alphabet = list (['a','b','c','d','e','f','g','h','i','j','k','l','m',
                  'n','o','p','q','r','s','t','u','v','w','x','y','z'])
ladder_list = list()
in_value = input("Enter string: ")
in_value = list(in_value)
command = input ('Commands:\n'
                '1.a or b or c or .... etc.(To count one letter)\n'
                '2.Ladder (from highest amount to the lowest)\n'
                '3.All(for outputting all amounts of letters)\n'
                'Insert: ')
if command.isdigit():
    print("Wrong command!")
    exit()
if command == 'All':
    a = 0
    while a < 26:
        num_of_letter = in_value.count(alphabet[a])
        append_value = alphabet[a] + " - " + str(num_of_letter)
        ladder_list.append(append_value)
        a += 1
    print (','.join(map(str, ladder_list)))

elif command == 'Ladder':
    a = 0
    while a < 26:
        num_of_letter = in_value.count(alphabet[a])
        append_value = alphabet[a]+" - ", num_of_letter
        ladder_list.append(append_value)
        a+=1
    sorted_ladder = sorted(ladder_list, key=lambda x:x[1],reverse=True)
    print(','.join(map(str, sorted_ladder)))
else:
    print(command, "-", in_value.count(command))