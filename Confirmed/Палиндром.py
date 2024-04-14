
userWord = input("Введите слово: ")
reverseStr = ''
reverseWord = []
for i in userWord:
    reverseWord.append(i)
reverseWord.reverse()
for el in reverseWord:
    reverseStr += el
if reverseStr == userWord:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
