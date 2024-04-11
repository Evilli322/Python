containerList = []
containerCount = int(input("Количество контейнеров: "))
count = 0
while count != containerCount:
    containerWeight = int(input("Введите вес контейнера: "))
    if containerWeight > 200:
        print('Вес контейнера не может превышать 200!')
    else:
        containerList.append(containerWeight)
        count += 1
while True:
    containerNew = int(input("Введите вес нового контейнера: "))
    if containerNew > 200:
        print('Вес контейнера не может превышать 200!')
    else:
        break
for i in range(containerCount - 1, -1, -1):
    if containerList[i] == containerNew:
        containerList.insert(i + 1, containerNew)
        print("Номер, который получит новый контейнер:", i + 2)
        break
    elif containerList[i] > containerNew:
        containerList.insert(i + 1, containerNew)
        index = containerList.index(containerNew)
        print("Номер, который получит новый контейнер:", containerList.index(containerNew) + 1)
        break
    elif containerList[0] < containerNew:
        containerList.insert(0, containerNew)
        print("Номер, который получит новый контейнер:", 1)
        break
