digitsList = [1, 2, 3, 4, 5]
digitsCount = len(digitsList)
shiftCount = int(input("Сдвиг: "))

for i in range(shiftCount):
    digitsList.insert(0, digitsCount - i)
    del digitsList[-1]
print(digitsList)
