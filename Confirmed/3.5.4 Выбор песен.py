violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time = 0
print("Список песен: ")
for i_elem in violator_songs:
    print(i_elem)
songs_count = int(input('Сколько песен выбрать? '))
for i in range(songs_count):
    user_song = input(f"Название {i + 1}-й песни: ")
    for i_elem in violator_songs:
        if i_elem[0] == user_song:
            time += i_elem[1]
print(f'Общее время звучания песен — {time} минуты')

