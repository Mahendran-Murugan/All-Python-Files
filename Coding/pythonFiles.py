file = open("mahi.txt")
txtRead = file.read()
for i in range(int(input())):
    inputStr = input()
    if inputStr in txtRead.strip():
        print(txtRead.count(inputStr))
    else:
        print(0)
