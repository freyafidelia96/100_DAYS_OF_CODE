def add(n1, n2):
    """Add two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """divide two numbers"""
    return round(n1 / n2, 2)


def calculator():

    num1 = eval(input("What's the first number? "))
    operations = {"+": add, 
                "-": subtract,
                "*": multiply, 
                "/": divide
                }

    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue == True:
        operation_symbol = input("Pick an operation\n")
        num2 = eval(input("What's the next number? "))

        computation = operations[operation_symbol]
        answer = computation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: " ).lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
