print("Insert value:")
in_value = int(input())
if (in_value < 0 ):
    print("Seconds can not be a negative value")
    exit()
days = in_value // 86400
in_value = in_value % 86400
hours = in_value // 3600
minutes = (in_value%3600) // 60
seconds = in_value % 60
print("Days:",days,"Hours:",hours,"Minutes:",minutes,"Seconds:",seconds)