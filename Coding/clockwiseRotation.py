def RotateNCompare():
    input_str1 = input()
    input_str2 = input()
    k = int(int(input()))
    for i in range(1, k):
        input_str1 = input_str1[1:]+input_str1[0]
    if input_str1 == input_str2:
        print("YES")
    else:
        print("NO")


RotateNCompare()
RotateNCompare()
