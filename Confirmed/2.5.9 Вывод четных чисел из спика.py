numbersList = [12, 2, 21, 32, 45, 98, 74, 17, 65, 10]
indexCount = len(numbersList)
for i in range(indexCount - 1, -1, -1):
    if numbersList[i] % 2 == 0:
        print(numbersList[i])

