input_str = input()
output_str = ""
count = 1
i = 0
while i < (len(input_str)-1):
    if input_str[i] is input_str[i+1]:
        count += 1
        i += 1
    else:
        output_str += f'{count}{input_str[i]}'
        count = 1
        i += 1
        continue
output_str += f'{count}{input_str[i]}'

print(output_str)
