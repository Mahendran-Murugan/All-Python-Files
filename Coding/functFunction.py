def add(a, b):
    return a + b


# Funct Keyword is used to pass a Function as Parameter to another Function
def fun(funct, a, b):
    return funct(a, b)


# here add function is passed as parameter to fun
print(fun(add, 5, 2))