def count_letters(letter):
  global numCount, lettCount
  num = input("Введите цифру: ")
  lett = input("Введите букву: ")

  for char in letter:
    if char == num:
      numCount += 1
    elif char == lett:
      lettCount += 1


letter = input("Введите фразу")
numCount = 0
lettCount = 0
count_letters(letter)
print("Цифр:", numCount, "\nБукв:", lettCount)
