string = sorted(input("Enter string: "))
length = len(string)
def amount(string, lenght):
    last_elem = string.count(string[lenght - 1])
    print(string[lenght - 1], "-", last_elem)
    lenght -= last_elem
    if lenght == 0:
        quit()
    amount(string, lenght)

amount(string,length)
