print("The equation looks : ax^2+bx+c=0; a!=0")
print("Insert value а: ")
a = int(input())
if a == 0:
    print("a can not equal to 0")
    exit(0)
print("Insert b value: ")
b = int(input())
print("Insert c value: ")
c = int(input())
D = b**2 - 4*a*c
if D < 0:
    print("There is no answer with Discriminant < 0")
    exit()
if D == 0:
    x = -(b/(2*a))
if D > 0:
    x1 = ((-b)+D**(1/2))/(2*a)
    x2 = ((-b)-D**(1/2))/(2*a)
    print("x1=",x1,"x2:",x2)