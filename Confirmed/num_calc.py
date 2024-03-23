import math


def operation(num, count):

  active = int(input("1 - сумма цифр; 2 - наибольшая цифра; 3 - наименьшая цифра\n"))
  if active == 1:
    sum(num, count)
  elif active == 2:
    max(num, count)
  elif active == 3:
    min(num, count)
  else:
    print("Выберете действие!")
    operation(num, count)


def sum(num, count):
  sum = 0
  temp = 0
  for i in range(count):
    temp = math.fmod(num, 10)
    num //= 10
    sum += temp
  print(sum)


def max(num, count):
  big = 0
  temp = 0
  for i in range(count):
    temp = math.fmod(num, 10)
    num //= 10
    if big <= temp:
      big = temp
  print(big)


def min(num, count):
  small = num
  temp = 0
  for i in range(count):
    temp = math.fmod(num, 10)
    num //= 10
    if small > temp:
      small = temp
  print(small)

while True:
  num = int(input("Введите число: "))
  numCount = num
  count = 0
  while numCount != 0:
    count += 1
    numCount //= 10
  operation(num, count)