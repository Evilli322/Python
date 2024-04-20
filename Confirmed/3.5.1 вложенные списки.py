a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]


def num_count(num, operation_count):
    print("Количество цифр", num, "при", operation_count, "объединении:", a.count(num))
    if num == 5:
        for _ in range(a.count(num)):
            a.remove(num)


a.extend(b)
num_count(5, 'первом')
a.extend(c)
num_count(3, "втором")
print("Итоговый список:", a)
