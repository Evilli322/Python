import math


def nod(fir, sec):
  if fir >= sec:
    prev = fir
    cur = sec
    while True:
      rem = math.fmod(prev, cur)
      prev = cur
      cur = rem
      if rem == 0:
        print(prev)
        return False
  else:
    prev = sec
    cur = fir
    while True:
      rem = math.fmod(prev, cur)
      prev = cur
      cur = rem
      if rem == 0:
        print(prev)
        return False


fir = int(input("Введите первое число: "))
sec = int(input("Введите второе число: "))
nod(fir, sec)
