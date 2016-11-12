word = input('Введите слово: ')
arr = []

while word:
    arr.append(word)
    word = input('Введите слово: ')
    

for i in range(len(arr)):
    newword = arr[i]
    part1 = newword[:2]
    part2 = newword[3:]
    newword = part1 + part2
    print(newword[::-1])
