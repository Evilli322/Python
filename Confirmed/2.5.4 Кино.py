films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
user_films = []
check = 0
count = int(input("Введите количество фильмов: "))
for i in range(count):
    user_choice = input("Введите название фильма: ")
    for a in range(len(films)):
        if user_choice == films[a]:
            user_films.append(user_choice)
            check = 1
            break
    if check != 1:
        print("Ошибка: фильма", user_choice, "у нас нет :(")
    check = 0
print("Ваш список любимых фильмов:", *user_films)





