inputStr = input()
binary = inputStr.replace('a', '1').replace('b', '0')[::-1]
base = 2
power = 0
decimal = 0
for i in binary:
    temp = pow(base, power)
    power += 1
    decimal += int(i) * temp
print(decimal)
