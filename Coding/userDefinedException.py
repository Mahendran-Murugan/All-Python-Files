class RangeExceedException(Exception):
    pass


n = int(input("Enter a Number b/w 1 to 10: "))

if -1 < n < 11:
    print(n)

else:
    raise RangeExceedException(f" {n} Not in Range from 1 to 10")