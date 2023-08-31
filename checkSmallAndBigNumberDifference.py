li = list(map(int, input(). split()))
k = int(input())
larger_ele = []
smaller_ele = []
for i in li:
    if i > k:
        larger_ele.append(i)
    elif i == k:
        continue
    else:
        smaller_ele.append(i)

print(f'Smaller elements are: {smaller_ele}')
print(f'Larger elements are: {larger_ele}')
print(f'Difference is:{abs((len(smaller_ele))-(len(larger_ele)))}')
