calculator_art = """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

status = True

def calculator():
    global status
    
    print(calculator_art)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("\nOperations: + - * / ")
    operation_symbol = input("Enter the operation you want to perform: ")
    while status:
        first_answer = operations[operation_symbol]
        result = first_answer(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        want_to_continue = input("Want to perform a different operation? (y/n): ").lower()
        if want_to_continue == 'y':
            num3 = float(input("Enter a number: "))
            print("\nOperations: + - * / ")
            operation_symbol = input("Enter the operation you want to perform: ")
            second_answer = operations[operation_symbol]
            result = second_answer(result, num3)
            print(f"{result} {operation_symbol} {num3} = {result}")
        else:
            status = False
            calculator()


calculator()
