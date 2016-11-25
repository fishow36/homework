word = input('Введите слово: ')

for index, letter in enumerate(word):
    print(word[:-index])
    
