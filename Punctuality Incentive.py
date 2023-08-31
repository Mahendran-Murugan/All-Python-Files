dailyWages = int(input())
noOfDaysOnTime = int(input())
listOfDailyWages = []
for i in range(noOfDaysOnTime):
    listOfDailyWages.append(dailyWages)
    dailyWages += 200

print(sum(listOfDailyWages))
