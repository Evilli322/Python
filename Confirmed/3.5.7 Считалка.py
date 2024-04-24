def find_last_person(N, K):
    circle = list(range(1, N + 1))
    index = 0
    while len(circle) > 1:
        index = (index + K - 1) % len(circle)
        print(f"Выбывает человек под номером {circle[index]}")
        del circle[index]
    return circle[0]


N = int(input("Количество человек: "))
K = int(input("Какое число в считалке? "))

last_person = find_last_person(N, K)
print(f"\nОстался человек под номером {last_person}")
