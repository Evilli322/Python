shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Название детали: ')
detail_count = 0
detail_cost = 0
for i_elem in shop:
    if i_elem[0] == detail:
        detail_count += 1
        detail_cost += i_elem[1]
print('Количество деталей:', detail_count, '\nОбщая стоимость:', detail_cost)

