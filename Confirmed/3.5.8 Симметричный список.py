num_count = int(input('Количество чисел: '))
num_list = []
for _ in range(num_count):
    number = int(input('Число: '))
    num_list.append(number)
print('Последовательность: ', num_list)
extra_list = list(num_list)
rev_list = list(reversed(num_list))

while True:
    if rev_list != extra_list:
        del extra_list[0]
        del rev_list[len(rev_list) - 1]
    else:
        rev_list = list(reversed(num_list))
        for i in range(len(extra_list)):
            del rev_list[0]
        print(f'Нужно приписать чисел: {len(rev_list)}\nСами числа: {rev_list}')
        break
