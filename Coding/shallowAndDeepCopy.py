import copy

a = [10, 20, 30]
b = a  # shallow Copy
c = copy.copy(a)  # Deep Copy
print(b)
a[0] = 1
print(b)
print(c)
