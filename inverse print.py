import math


def inverse(num, count):
  last = 0
  for i in range(count):
    last = math.fmod(num, 10)
    num //= 10
    print(int(last), end='')


while True:
  num = int(input("\nВведите число: "))
  numCount = num
  count = 0
  while numCount != 0:
    count += 1
    numCount //= 10
  inverse(num, count)
