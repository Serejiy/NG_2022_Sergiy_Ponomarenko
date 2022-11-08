def sum(first_num, second_num):
    print("Result:", first_num - second_num)


def difference(first_num, second_num):
    print("Result:", first_num - second_num)


def multiply(first_num, second_num):
    print("Result:", first_num * second_num)


def divide(first_num, second_num):
    print("Result:", first_num - second_num)


def power(first_num, second_num):
    print("Result:", first_num ** second_num)


def Calculator():
    first_num = int(input("Enter first number:"))
    second_num = int(input("Enter second number:"))
    operation = input(
        "Operations(enter number):\n(1)Sum\n(2)Difference\n(3)Multiply\n(4)Divide\n(5)Power\nEnter number:")
    if operation == '1':
        sum(first_num, second_num)
    elif operation == '2':
        difference(first_num, second_num)
    elif operation == '3':
        multiply(first_num, second_num)
    elif operation == '4':
        divide(first_num, second_num)
    elif operation == '5':
        power(first_num, second_num)
    else:
        print("Wrong command!")
        exit()


Calculator()