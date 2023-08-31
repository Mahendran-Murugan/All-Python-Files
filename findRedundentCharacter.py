input_str = input()
dic = {}
for i in range(len(input_str)):
    count = input_str.count(input_str[i])
    dic[input_str[i]] = count

max_val = max(dic.values())
for i in dic.items():
    if i[1] == max_val:
        print(i[0])
        break


