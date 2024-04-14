N = int(input("Введите число: "))
Nlist = []
for i in range(N):
    if i % 2 != 0:
        Nlist.append(i)
print("Список из нечётных чисел от одного до N: ", Nlist)
