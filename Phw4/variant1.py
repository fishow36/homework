   
word = input('Введите слово: ')
print(word)
for index in range (1, len(word)):
    print(word[:-index])
