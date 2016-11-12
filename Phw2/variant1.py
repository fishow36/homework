word = input()
for index, letter in enumerate(word):
    if index % 2 != 0 and letter != 'а' and letter != 'к':
        print(letter)
