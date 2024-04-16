playersList = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
for i in range(len(playersList) - 1):
    if i % 2 == 0 or i == 0:
        print(playersList[i], end=', ')
