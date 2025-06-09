def divide(result , next_number):
    if next_number == 0:
        print('you can not divide by 0')
        return result
    else:
        print(f'{result} / {next_number} = {result / next_number}')
        return (result / next_number)

def multiply(result, next_number):
    print(f'{result} * {next_number} = {result * next_number}')
    return (result * next_number)
def add(result , next_number):
    print(f'{result} + {next_number} = {result + next_number}')
    return ( result + next_number)
def subtruct(result , next_number):
    print(f'{result} - {next_number} = {result - next_number}')
    return ( result - next_number)

result =int(input ('pick your first number: '))
print(' / \n * \n + \n -')
continue_calc = 'y'
while continue_calc.lower() == 'y' :
    operation = input('pick opertion : ')
    next_number = int(input('what is your next number? '))
    if operation == '/':
        result = divide(result, next_number)
    elif operation == '*':
        result = multiply(result , next_number)
    elif operation == '+':
        result = add(result , next_number)
    elif operation == '-':
        result = subtruct(result , next_number)
    else:
        operation = input('please enter a valid operation ')

    continue_calc = input('Type "y" to continue "n" to end calculation ')