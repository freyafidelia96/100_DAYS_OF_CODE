from flask import Flask, render_template, redirect, url_for, flash, request, send_file, jsonify
from flask_bootstrap import Bootstrap5
import os
from datetime import datetime as dt
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float, ForeignKey, DECIMAL, and_, or_
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignUp, Login
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



YEAR = dt.now().year

# Initialize Flask and AWS Polly
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = os.getenv('PAYSTACK_PUBLIC_KEY')


Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///posts.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(Text, nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Relationship to Cart
    cart = relationship("Cart", back_populates="shopper", uselist=False)  # A user has one cart
    # Relationship to Orders
    orders = relationship("Order", back_populates="shopper")  # A user can have multiple orders

# Cart model
class Cart(db.Model):
    __tablename__ = "carts"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shopper_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    shopper = relationship("Users", back_populates="cart")
    created_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    cart_items = relationship("CartItems", back_populates="cart")


# Product model
class Product(db.Model):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    thumbnail: Mapped[str] = mapped_column(String(250))
    category: Mapped[str] = mapped_column(String(250))
    created_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    updated_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))


# CartItems model
class CartItems(db.Model):
    __tablename__ = "cart_items"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("carts.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    
    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product")


# Orders model
class Order(db.Model):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shopper_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    total_price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    shipping_address: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    updated_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))

    # Relationship with User
    shopper = relationship("Users", back_populates="orders")
    # Relationship with OrderItems
    order_items = relationship("OrderItem", back_populates="order")
    # Relationship with Payment
    payment = relationship("Payment", back_populates="order", uselist=False)  # One-to-One relationship


# OrderItems model
class OrderItem(db.Model):
    __tablename__ = "order_items"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)  # Price at the time of purchase
    
    # Relationships
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product")


# Payments model
class Payment(db.Model):
    __tablename__ = "payments"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"))
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    payment_method: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    payment_date: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Relationship with Order
    order = relationship("Order", back_populates="payment")

    
with app.app_context():
    db.create_all()

products = [
    {
        "id": 1,
        "name": "Ace Elec 20000 mAh Ultra Slim Portable Power Bank",
        "description": "A powerful and slim power bank with 20,000 mAh capacity. Ideal for on-the-go charging.",
        "price": 8200.00,
        "stock": 23,
        "category": "Electronics",
        "thumbnail": "static/images/powerBank.jpg",
        "created_at": "2024-10-04 14:30:25",
        "updated_at": "2024-10-04 14:30:25"
    },
    {
        "id": 2,
        "name": "Wireless Bluetooth Earbuds - Noise Cancelling",
        "description": "High-quality Bluetooth earbuds with noise cancellation for crystal-clear sound.",
        "price": 15000.00,
        "stock": 50,
        "category": "Electronics",
        "thumbnail": "static/images/earpods.jpg",
        "created_at": "2024-10-04 15:12:00",
        "updated_at": "2024-10-04 15:12:00"
    },
    {
        "id": 3,
        "name": "Men's Slim Fit Denim Jeans",
        "description": "Stylish slim-fit jeans perfect for casual wear. Available in various sizes.",
        "price": 5000.00,
        "stock": 100,
        "category": "Fashion",
        "thumbnail": "static/images/DenimJeans.jpg",
        "created_at": "2024-10-04 16:20:45",
        "updated_at": "2024-10-04 16:20:45"
    },
    {
        "id": 4,
        "name": "Luxury Women's Handbag - Leather",
        "description": "Elegant leather handbag for women, perfect for both casual and formal occasions.",
        "price": 25000.00,
        "stock": 15,
        "category": "Fashion",
        "thumbnail": "static/images/Handbag.jpg",
        "created_at": "2024-10-04 17:05:30",
        "updated_at": "2024-10-04 17:05:30"
    },
    {
        "id": 5,
        "name": "Electric Hair Clipper - Professional",
        "description": "Professional electric hair clipper with adjustable blades for precise trimming.",
        "price": 6500.00,
        "stock": 35,
        "category": "Health",
        "thumbnail": "static/images/hairclipper.avif",
        "created_at": "2024-10-04 17:50:10",
        "updated_at": "2024-10-04 17:50:10"
    },
    {
        "id": 6,
        "name": "Vitamin C Serum for Face - 30ml",
        "description": "Brighten and rejuvenate your skin with this high-quality Vitamin C serum.",
        "price": 3500.00,
        "stock": 60,
        "category": "Beauty",
        "thumbnail": "static/images/FaceSerum.jpg",
        "created_at": "2024-10-04 18:22:55",
        "updated_at": "2024-10-04 18:22:55"
    },
    {
        "id": 7,
        "name": "Wireless Charging Pad - Fast Charge",
        "description": "Fast-charging wireless pad compatible with a wide range of devices.",
        "price": 4000.00,
        "stock": 75,
        "category": "Electronics",
        "thumbnail": "static/images/wirelessPAd.jpg",
        "created_at": "2024-10-04 18:45:00",
        "updated_at": "2024-10-04 18:45:00"
    },
    {
        "id": 8,
        "name": "Men's Leather Belt - Brown",
        "description": "Classic brown leather belt for men, perfect for formal and casual attire.",
        "price": 3500.00,
        "stock": 80,
        "category": "Fashion",
        "thumbnail": "static/images/Belt.jpg",
        "created_at": "2024-10-04 19:05:20",
        "updated_at": "2024-10-04 19:05:20"
    },
    {
        "id": 9,
        "name": "Women's Perfume - 50ml",
        "description": "A refreshing and long-lasting fragrance designed for women.",
        "price": 12000.00,
        "stock": 40,
        "category": "Beauty",
        "thumbnail": "static/images/perfume.jpg",
        "created_at": "2024-10-04 19:30:45",
        "updated_at": "2024-10-04 19:30:45"
    },
    {
        "id": 10,
        "name": "Infrared Thermometer - Non-Contact",
        "description": "Measure body temperature accurately with this non-contact infrared thermometer.",
        "price": 7500.00,
        "stock": 25,
        "category": "Health",
        "thumbnail": "static/images/therm.jpg",
        "created_at": "2024-10-04 20:00:10",
        "updated_at": "2024-10-04 20:00:10"
    },
     {
        "id": 11,
        "name": "Smart LED TV 43 Inch - Full HD",
        "description": "Full HD 43-inch smart TV with vibrant display.",
        "price": 120000.00,
        "stock": 12,
        "category": "Electronics",
        "thumbnail": "static/images/TV.jpg",
        "created_at": "2024-10-04 20:30:00",
        "updated_at": "2024-10-04 20:30:00"
    },
    {
        "id": 12,
        "name": "Women's Sneakers - White",
        "description": "Stylish white sneakers for everyday wear.",
        "price": 8500.00,
        "stock": 45,
        "category": "Fashion",
        "thumbnail": "static/images/sneakers.jpg",
        "created_at": "2024-10-04 20:45:15",
        "updated_at": "2024-10-04 20:45:15"
    },
    {
        "id": 13,
        "name": "Electric Toothbrush - Rechargeable",
        "description": "Rechargeable electric toothbrush for a perfect clean.",
        "price": 4500.00,
        "stock": 30,
        "category": "Health",
        "thumbnail": "static/images/Toothbrush.jpg",
        "created_at": "2024-10-04 21:00:20",
        "updated_at": "2024-10-04 21:00:20"
    },
    {
        "id": 14,
        "name": "Lipstick Set - 5 Colors",
        "description": "Vibrant lipstick set with five shades.",
        "price": 3500.00,
        "stock": 60,
        "category": "Beauty",
        "thumbnail": "static/images/lipstick.jpg",
        "created_at": "2024-10-04 21:15:30",
        "updated_at": "2024-10-04 21:15:30"
    },
    {
        "id": 15,
        "name": "Men's Leather Watch - Black",
        "description": "Elegant leather watch with a classic black design.",
        "price": 10500.00,
        "stock": 25,
        "category": "Fashion",
        "thumbnail": "static/images/watch.jpg",
        "created_at": "2024-10-04 21:30:40",
        "updated_at": "2024-10-04 21:30:40"
    },
    {
        "id": 16,
        "name": "Gaming Mouse - RGB Lighting",
        "description": "High-precision gaming mouse with RGB lighting.",
        "price": 6000.00,
        "stock": 35,
        "category": "Electronics",
        "thumbnail": "static/images/mouse.jpg",
        "created_at": "2024-10-04 21:45:55",
        "updated_at": "2024-10-04 21:45:55"
    },
    {
        "id": 17,
        "name": "Hair Dryer - 1800W",
        "description": "Powerful 1800W hair dryer for fast drying.",
        "price": 7200.00,
        "stock": 40,
        "category": "Beauty",
        "thumbnail": "static/images/hairDryer.jpg",
        "created_at": "2024-10-04 22:00:10",
        "updated_at": "2024-10-04 22:00:10"
    },
    {
        "id": 18,
        "name": "Digital Kitchen Scale - 5kg Capacity",
        "description": "Precision kitchen scale with 5kg capacity.",
        "price": 2500.00,
        "stock": 55,
        "category": "Electronics",
        "thumbnail": "static/images/scale.jpg",
        "created_at": "2024-10-04 22:15:20",
        "updated_at": "2024-10-04 22:15:20"
    },
    {
        "id": 19,
        "name": "Face Moisturizer - 100ml",
        "description": "Hydrating face moisturizer for daily use.",
        "price": 1800.00,
        "stock": 80,
        "category": "Beauty",
        "thumbnail": "static/images/faceMoisturizer.jpg",
        "created_at": "2024-10-04 22:30:30",
        "updated_at": "2024-10-04 22:30:30"
    },
    {
        "id": 20,
        "name": "Blood Pressure Monitor - Digital",
        "description": "Accurate digital blood pressure monitor for home use.",
        "price": 9000.00,
        "stock": 20,
        "category": "Health",
        "thumbnail": "static/images/bloodpressure.jpg",
        "created_at": "2024-10-04 22:45:45",
        "updated_at": "2024-10-04 22:45:45"
    }
]


@app.route('/')
def home():
    for product in products:
        new_product = Product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            stock=product['stock'],
            category=product['category'],
            thumbnail=product['thumbnail']
        )

        db.session.add(new_product)
        db.session.commit()
    products = db.session.execute(db.select(Product)).scalars().all()
    return render_template('index.html', products=products, current_user=current_user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():

        email_same = db.session.execute(db.select(Users).where(Users.email == form.email.data)).scalar()

        username_same = db.session.execute(db.select(Users).where(Users.username == form.username.data)).scalar()

        if username_same:
            flash("The username you entered is already taken. Please choose a different username.")
            return redirect(url_for('signup'))

        if email_same:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('signup'))

        hashed_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = Users(
            username = form.username.data,
            full_name = form.fullName.data,
            email = form.email.data,
            password = hashed_salted_password,
            address = form.address.data,
            phone_number = form.phoneNumber.data
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signUp.html', form=form, current_user=current_user)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    password = form.password.data

    if form.validate_on_submit():
        user = db.session.execute(db.select(Users).where(Users.email == form.email.data)).scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
        
    return render_template('login.html', form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/view-product/<product_id>')
def view_product(product_id):
    product = db.session.execute(db.select(Product).where(Product.id == product_id)).scalar()

    product_price = "{:,}".format(product.price)
    return render_template('product.html', product=product, product_price=product_price, current_user=current_user)




@app.route('/cart/<product_id>')
@login_required
def add_to_cart(product_id):
    user = current_user

    cart = db.session.execute(db.select(Cart).where(Cart.shopper_id == user.id)).scalar()

    if not cart:
        new_cart = Cart(
            shopper_id = user.id
        )
        db.session.add(new_cart)
        db.session.commit()

        cart = db.session.execute(db.select(Cart).where(Cart.shopper_id == user.id)).scalar()

    cart_item = db.session.execute(db.select(CartItems).where(and_(CartItems.cart_id == cart.id, CartItems.product_id == product_id))).scalar()

    if not cart_item:  
        new_cart_item = CartItems(
            cart_id = cart.id,
            product_id = product_id      
        )

        db.session.add(new_cart_item)
        db.session.commit()

    return redirect(url_for('show_cart', cart_id=cart.id, current_user=current_user))

    

@app.route('/show-cart/<cart_id>')
@login_required
def show_cart(cart_id):
    print(cart_id)
    cart = db.session.execute(db.select(Cart).where(Cart.id == cart_id)).scalar()
    cart_items = cart.cart_items
    sum = 0
    for item in cart_items:
        sum += item.product.price * item.quantity

    formatted_sum = "{:,}".format(sum)

    return render_template('show_cart.html', cart_items=cart_items, sum=formatted_sum, cart_id=cart_id, current_user=current_user)



@app.route('/add-quantity/<item_id>')
@login_required
def add_quantity(item_id):
    item = db.get_or_404(CartItems, item_id)
    cart_id = item.cart_id
    stock_amount = item.product.stock

    if item.quantity < stock_amount:
        item.quantity += 1
        db.session.commit()
    else:
        flash('Out of stock')

    return redirect(url_for("show_cart", cart_id=cart_id, current_user=current_user))


@app.route('/sub-quantity/<item_id>')
@login_required
def sub_quantity(item_id):
    item = db.get_or_404(CartItems, item_id)
    cart_id = item.cart_id
    if item.quantity > 1:
        item.quantity -= 1
    db.session.commit()

    return redirect(url_for("show_cart", cart_id=cart_id, current_user=current_user))


@app.route('/delete/<item_id>')
@login_required
def delete(item_id):
    item = db.session.execute(db.select(CartItems).where(CartItems.id == item_id)).scalar()
    cart_id = item.cart_id
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("show_cart", cart_id=cart_id, current_user=current_user))



@app.route('/verify_payment/<reference>', methods=['GET'])
@login_required
def verify_payment(reference):
    """Verify Paystack payment using the reference from the frontend"""
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json',
    }
    
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if data['status'] and data['data']['status'] == 'success':
        # Payment was successful
        return jsonify({'message': 'Payment verification successful', 'data': data}), 200
    else:
        # Payment failed or invalid reference
        return jsonify({'message': 'Payment verification failed', 'data': data}), 400


@app.route('/checkout/<cart_id>/<sum>', methods=['GET', 'POST'])
@login_required
def checkout(cart_id, sum):

    cart = db.session.execute(db.select(Cart).where(Cart.id == cart_id)).scalar()
    cart_items = cart.cart_items
    unformatted_sum = float(sum.replace(',', '')) * 100

    if request.method == "POST":
        new_order = Order(
            shopper_id = cart.shopper_id,
            total_price = unformatted_sum / 100,
            shipping_address = request.form.get('address')
        )
        
        db.session.add(new_order)
        db.session.commit()

        order = db.session.execute(db.select(Order).where(Order.shopper_id == cart.shopper_id)).scalars().all()
        order_id = order[-1].id

        new_payment = Payment(
            order_id = order_id,
            amount = unformatted_sum / 100,
            payment_method = 'Paystack'
        )

        db.session.add(new_payment)
        db.session.commit()

        for item in cart_items:
            new_order_items = OrderItem(
                order_id = order_id,
                product_id = item.product_id,
                quantity = item.quantity,
                price = item.product.price
            )

            db.session.add(new_order_items)
            db.session.commit()


    return render_template('checkout.html', cart=cart, cart_items=cart_items, sum=sum, PAYSTACK_PUBLIC_KEY=PAYSTACK_PUBLIC_KEY, current_user=current_user, unformatted_sum=unformatted_sum)


@app.route('/categories/<category>')
def categories(category):
    if '&' in category:
        first_category = category.split('&')[0]
        second_category = category.split('&')[1]
        category_ = db.session.execute(db.select(Product).where(or_(Product.category == first_category, Product.category == second_category)))
        products = category_.scalars().all()
        category = first_category + " & " + second_category
    else:
        category_ = db.session.execute(db.select(Product).where(Product.category == category))
        products = category_.scalars().all()

    return render_template('category.html', products=products, category=category, current_user=current_user)
    

@app.route('/order')
@login_required
def order():
    shopper_id = current_user.id

    orders = db.session.execute(db.select(Order).where(Order.shopper_id == shopper_id)).scalars().all()

    return render_template('order.html', orders=orders, current_user=current_user)


@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_query = request.form.get('query')

        print(search_query)

        if search_query:
            # Search for products that match the search query (case-insensitive)
            results = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()

            # Pass the results to the template to display
            return render_template('search.html', query=search_query, results=results)

    # If no query, return an empty results page
    return render_template('search.html', query=search_query, results=[])


if __name__ == '__main__':
    app.run(debug=True)