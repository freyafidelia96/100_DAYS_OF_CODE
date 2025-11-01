from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, desc
from datetime import datetime as dt
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do-list.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Todo(db.Model):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Unique ID
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)  # Task title
    description: Mapped[str] = mapped_column(String, nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)  # Task completion status
    created_at: Mapped[str] = mapped_column(String, default=dt.now().strftime('%Y-%m-%d %H:%M:%S'))  # Task creation time
    due_date: Mapped[str] = mapped_column(String, nullable=False)  # Optional deadline for the task

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    

with app.app_context():
    db.create_all()

@app.route('/todos')
def todos():
    todos = db.session.execute(db.select(Todo).order_by(desc(Todo.created_at))).scalars().all()
    return jsonify(todos=[todo.to_dict() for todo in todos]), 200


@app.route('/todo')
def todo():
    title = request.args.get('title')

    todo = db.session.execute(db.select(Todo).where(Todo.title == title)).scalar()

    error = {"Not Found": "Sorry, we don't have a todo by that title"}

    if todo:
        return jsonify(todo=todo.to_dict()), 200
    else:
        return jsonify(error=error), 404



@app.route('/add', methods=['POST'])
def add():
    due_date_str = request.form.get('due_date')

    if due_date_str:
        due_date = dt.strptime(due_date_str, '%Y-%m-%d')
    else:
        due_date = None

    new_todo = Todo(
        title = request.form.get('title'),
        description = request.form.get('description'),
        due_date = due_date
    )

    db.session.add(new_todo)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new todo."}), 200


@app.route('/update-todo/<todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    try:
        todo = db.get_or_404(Todo, todo_id)

        title = request.args.get('title')
        description = request.args.get('description')
        due_date = request.args.get('due_date')

        if title:
            todo.title = title
        if description:
            todo.description = description
        if due_date:
            todo.due_date = dt.strptime(due_date, '%Y-%m-%d')
        
        db.session.commit()

    except Exception:
        return jsonify(error={"Not Found": "Sorry, a todo with that id was not found in the database"}), 404
    
    else:
        return jsonify(response={"success": "Successfully updated the todo."}), 200


@app.route('/delete-todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):

    inputted_api_key = request.args.get('api-key')

    api_key = os.environ.get('API_KEY')

    if inputted_api_key == api_key:
        try:
            todo = db.get_or_404(Todo, todo_id)

            db.session.delete(todo)
            db.session.commit()

        except Exception:
            return jsonify(error={"Not Found": "Sorry, a todo with that id was not found in the database"}), 404
        
        else:
            return jsonify(response={"success": "Successfully deleted the todo."}), 200
        
    else:
        print(api_key)
        return jsonify({'error':"Sorry, that's is not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)


    