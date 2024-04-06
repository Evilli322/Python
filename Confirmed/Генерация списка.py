N = int(input("Введите число: "))
numbers_list = []
for i in range(N + 1):
    if i % 2 != 0:
        numbers_list.append(i)
print("Список из нечётных чисел от одного до N: ", numbers_list)

