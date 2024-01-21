# Map is Used to Map one to Another Type

intCollection = [10, 20, 30, 40]
floatCollection = list(map(float, intCollection))
print(floatCollection)


# Filter is Used to Filter data on Condition

ages = [10, 20, 30, 40, 17, 2]
adults = list(filter(lambda x: x >= 18, ages))
print(adults)