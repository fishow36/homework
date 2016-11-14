word = input('Введите слово: ')
arr = []

while word:
    arr.append(word)
    word = input('Введите слово: ')
    

for i in range(len(arr)):
    newword = arr[i]
    newword = list(newword[::-1])
    for j in range (len(newword)):
        if (j+1)%3 == 0:
            newword[j] = ''
    newword = ''.join(newword)
    print(newword)
