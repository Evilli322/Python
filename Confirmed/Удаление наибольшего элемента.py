max_card = 0
vc_list = []
new_list = []
count = int(input("Количество видеокарт: "))

for i in range(count):
    print('Видеокарта', i + 1, end="")
    card = int(input(': '))
    vc_list.append(card)
    if card > max_card:
        max_card = card
print("Старый список видеокарт:", vc_list)
for i in range(len(vc_list)):
    if max_card != vc_list[i]:
        new_list.append(vc_list[i])
print("Новый список видеокарт:", new_list)




