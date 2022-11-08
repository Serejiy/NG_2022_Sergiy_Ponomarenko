print("Choose operation (+,-,*,/,root(квадратный корень),power(степень): ")
in_value = input()
print("Insert first value: ")
first_value = int (input ())
print("Insert second value: ")
second_value = int(input())
if in_value == "+":
    print(first_value+second_value)
if in_value == "-":
    print(first_value-second_value)
if in_value == "*":
    print(first_value*second_value)
if in_value == "/":
    print(first_value/second_value)
if in_value == "root":
    print(first_value**(1/2), "," ,second_value**(1/2))
if in_value == "power":
    print(first_value**second_value)