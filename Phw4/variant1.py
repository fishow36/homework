   
word = input('Введите слово: ')
word = word + ' '
for index in range (len(word)):
    print(word[:-index])
