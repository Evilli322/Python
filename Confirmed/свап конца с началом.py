def count_numbers(temp):
  count = 0
  while temp > 0:
    count += 1
    temp //= 10 
  return count

def change_number(temp, count):
  last_digit = temp % 10
  first_digit = temp // 10 ** (count - 1)
  between_digits = temp % 10 ** (count - 1) // 10
  temp = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
  return temp

def Main():
  first_n = int(input("Введите первое число: "))
  temp = first_n
  count = count_numbers(first_n)
  if count < 3:
    print("В первом числе меньше трёх цифр.")
  else:
    first_n = change_number(temp, count)
    print('Изменённое первое число:', first_n)
  second_n = int(input("\nВведите второе число: "))
  temp = second_n
  count = count_numbers(second_n)
  if count < 4:
     print("Во втором числе меньше четырёх цифр.")
  else:
    second_n = change_number(temp, count)
    print('Изменённое второе число:', second_n)
    print('\nСумма чисел:', first_n + second_n)
Main()

