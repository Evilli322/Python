def maximum_of_two(temp1, temp2):
  if temp1 >= temp2:
    return temp1
  else:
    return temp2

def maximum_of_three(first, second, thrid):
  temp1 = first
  temp2 = second
  temp = maximum_of_two(temp1, temp2)
  temp1 = temp
  temp2 = thrid
  print(maximum_of_two(temp1, temp2))

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
thrid = int(input("Введите третье число: "))
maximum_of_three(first, second, thrid)