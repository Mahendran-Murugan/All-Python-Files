def square(num):
    for i in range(num):
        yield i*i


dic = {}
n = tuple(square(3))
for i, e in enumerate(n):
    dic[i] = e

print(dic)

*n, = "mahi"
print(n)