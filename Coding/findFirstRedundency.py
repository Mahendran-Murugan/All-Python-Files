def firstRedundant():
    input_str = input()
    dic = {}
    for i in range(0, len(input_str)):
        try:
            index = input_str.index(input_str[i], i + 1)
            dic[input_str[i]] = index
        except ValueError as e:
            continue

    min_val = min(dic.values())

    for i in dic.items():
        if i[1] == min_val:
            print(i[0])


firstRedundant()
firstRedundant()
