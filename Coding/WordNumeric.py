input_str = input()
output_str = ''
i = 0
j = 1
carry = ''
while i < (len(input_str)):
    if input_str[i].isalpha():
        while j < (len(input_str)):
            if input_str[i+j].isdigit():
                carry += input_str[i+j]
                j += 1
                if i+j >= len(input_str):
                    break
                continue
            else:
                j += 1
                break
        output_str += f'{input_str[i] * int(carry)}'
        i += 1
    else:
        i += 1
        j = 1
        carry = ''
        continue

print(output_str)
