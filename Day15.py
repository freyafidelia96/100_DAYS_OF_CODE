resources = {"Water": 500, "Milk": 300, "Coffee": 100, "Money": 0.0}

def cal_resources(user_answer):
    if user_answer == 'espresso':
        if resources['Water'] < 50:
            return print(f"Sorry there's not enough water")
        else:
            resources['Water'] = resources['Water'] - 50
        
        if resources['Coffee'] < 18:
            return print(f"Sorry there's not enough coffee")
        else:
            resources['Coffee'] = resources['Coffee'] - 18
        print(f"Here's you cup of coffee \u2615")
    elif user_answer == 'latte':
        if resources['Water'] < 200:
            return print(f"Sorry there's not enough water")
        else:
            resources['Water'] = resources['Water'] - 200
        
        if resources['Coffee'] < 24:
            return print(f"Sorry there's not enough coffee")
        else:
            resources['Coffee'] = resources['Coffee'] - 24

        if resources['Milk'] < 150:
            return print(f"Sorry there's not enough milk")
        else:
            resources['Milk'] = resources['Milk'] - 150
        print(f"Here's you cup of coffee \u2615")
    elif user_answer == 'cappuccino':
        if resources['Water'] < 250:
            return print(f"Insufficient resources")
        else:
            resources['Water'] = resources['Water'] - 250
        
        if resources['Coffee'] < 24:
            return print(f"Insufficient resources")
        else:
            resources['Coffee'] = resources['Coffee'] - 24

        if resources['Milk'] < 100:
            return print(f"Insufficient resources")
        else:
            resources['Milk'] = resources['Milk'] - 100
        print(f"Here's you cup of coffee \u2615")

    else:
        return print("Invalid input.")

def cal_money(user_answer):
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    if user_answer == 'espresso':
        if total < 1.50:
            return print(f"Sorry that's not enough money. Money refunded.")
        else:
            resources['Money'] = resources['Money'] + 1.50
            if total > 1.50:
                print(f"Here' ${round(total - 1.50, 2)} in change")
    if user_answer == 'latte':
        if total < 2.50:
            return print(f"Sorry that's not enough money. Money refunded.")
        else:
            resources['Money'] = resources['Money'] + 2.50
            if total > 2.50:
                print(f"Here' ${round(total - 2.50, 2)} in change")
    if user_answer == 'cappuccino':
        if total < 3.00:
            return print(f"Sorry that's not enough money. Money refunded.")
        else:
            resources['Money'] = resources['Money'] + 3.00
            if total > 3.00:
                print(f"Here' ${round(total - 3.00, 2)} in change")
    cal_resources(user_answer)
            
def main():
    user_answer = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer == 'off':
        return
    elif user_answer == 'report':
        print(f"Water: {resources['Water']}ml \nMilk {resources['Milk']}ml \nCoffee: {resources['Coffee']}g \nMoney: ${resources['Money']}")
    
    else:
        cal_money(user_answer)
    main()

if __name__ == "__main__":
    main()