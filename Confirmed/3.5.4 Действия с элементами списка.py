guests = ["Петя", 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    action = input("Гость пришёл или ушёл? ")
    if action == 'пришел' and len(guests) <= 5:
        guest_name = input("Имя гостя: ")
        guests.append(guest_name)
        print(f'Привет, {guest_name}!')
    elif action == 'пришел' and (len(guests) == 6 or len(guests) == 0):
        guest_name = input("Имя гостя: ")
        print(f'Прости, {guest_name}, но мест нет.')
    elif action == 'ушел':
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f'Пока, {guest_name}!')
    elif action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
