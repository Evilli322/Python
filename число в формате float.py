import math


#math.ceil(num) - найти первую цифру != 0
def calc(num):

  if num < 1:
    rev = int(math.trunc(1 / num))
    count = 0
    while rev > 0:
      rev //= 10
      count += 1

    print(num * 10**count, "* 10 **", -count)
  elif num >= 1:
    count = 0
    rev = num
    while rev > 0:
      rev //= 10
      count += 1
    print(num / 10**(count - 1), "* 10 **", count - 1)


num = 0
while num <= 0:
  num = float(input("Введите число больше нуля: "))
calc(num)
