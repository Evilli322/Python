def reverse(temp):
  count = 0
  result = 0
  cycle = temp
  while cycle > 0:
    cycle //= 10
    count += 1
  for i in range(count, 0, -1):
    result += temp % 10 * 10 ** (i - 1)
    temp //= 10
  return result

def func(N,K): 
  sum = 0
  temp = N
  output = reverse(temp)
  sum += output
  print("Первое число наоборот:", output)
  temp = K
  output = reverse(temp)
  sum += output
  print("Второе число наоборот:", output)
  print("Сумма:", sum)
  temp = sum
  print("Сумма наоборот:", reverse(temp))

N = int(input("Введите первое число: "))
K = int(input("Введите второе число: "))
func(N, K)