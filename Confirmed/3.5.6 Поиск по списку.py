roller_sizes = [41, 40, 39, 42]
rollers = 0
print('Количество роликов:', len(roller_sizes))
for i in range(len(roller_sizes)):
    print(f'Размер пары {i + 1}: {roller_sizes[i]}')
human_count = int(input('Количество людей: '))
for i in range(human_count):
    leg_size = int(input(f'Размер ноги человека {i + 1}: '))
    for i_elem in roller_sizes:
        if i_elem == leg_size:
            rollers += 1
print("Наибольшее количество людей, которые могут взять ролики:", rollers)
