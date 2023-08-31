input_name = input()
for i in range(0, len(input_name)):
    for j in range(0, len(input_name)):
        if i == 0 or j == 0 or i == len(input_name)-1 or j == len(input_name)-1:
            print(input_name[j], end='')
        else:
            print(" ", end='')
    print()
