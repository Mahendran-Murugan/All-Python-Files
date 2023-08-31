def replaceUnitDigitWithZero():
    num = int(input())
    temp = num
    unitDigit = temp % 10
    last10 = 1
    outputNum = 0
    while temp != 0:
        lastDigit = temp % 10
        temp //= 10
        last10 *= 10
        if lastDigit == unitDigit:
            if temp != 0:
                outputNum = temp * last10
            else:
                last10 //= 10
                outputNum -= unitDigit * last10
    print(outputNum)


replaceUnitDigitWithZero()
replaceUnitDigitWithZero()
