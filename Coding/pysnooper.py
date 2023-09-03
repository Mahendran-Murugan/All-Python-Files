import pysnooper
from pysnooper import *

@pysnooper.number
def number(x, y):
    z = x + y
    return z


print(number(5, 6))
