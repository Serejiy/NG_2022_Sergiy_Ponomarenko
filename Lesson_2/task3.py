in_value = int(input("Enter value: "))
for a in range(in_value):
    for b in range(in_value - a):
        print(in_value - a - b, end=" ")
    print()