from art import logo

print(logo)


#  Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What is the first number?: "))
    should_continue = True

    while should_continue:
        not_symbol = True
        operation_symbol = ''
        while operation_symbol not in operations:
            operation_symbol = input("Pick and operation:  Type '+', '-', '*', or '/' ")
        num2 = float(input('What is the next number?: '))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
