import random


def rock_paper_scissors():
  rand = random.randint(1, 3)
  temp = int(input("1 - Камень, 2 - ножницы, 3 - бумага\n"))
  #Ничья
  if rand == temp:
    print("Ничья!")

  elif temp == 1 and rand == 2:  #Победа - камень
    print("Победа! Камень бьёт ножницы")
  elif temp == 1 and rand == 3:  #Поражение - камень
    print("Поражение! Бумага кроет камень")
  elif temp == 2 and rand == 3:  #Победа - ножницы
    print("Победа! Ножницы режут бумагу")
  elif temp == 2 and rand == 1:  #Поражение - ножницы
    print("Поражение! Камень бьёт ножницы")
  elif temp == 3 and rand == 1:  #Победа - бумага
    print("Победа! Бумага кроет камень")
  elif temp == 3 and rand == 2:  #Поражение - бумага
    print("Поражение! Ножницы режут бумагу")


def guess_the_number():
  rand = random.randint(1, 10)
  temp = 0
  while rand != temp:
    temp = int(input("Введите число от 1 до 10"))
  print("Вы угадали! ")


def mainMenu():
  choice = int(
      input(
          "Выберете игру:\n 1 - Камень, ножницы, бумага\n 2 - угадай число\n"))
  if choice == 1:
    rock_paper_scissors()
  elif choice == 2:
    guess_the_number()
  else:
    mainMenu()


mainMenu()
