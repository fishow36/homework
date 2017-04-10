import os
import shutil
number = int(input('Введите число: '))
for i in range (1, number+1):
    os.mkdir(str(i))
    for j in range(1, i+1):
        open (str(i)+'\\text'+str(j) + '.txt', 'w', encoding = 'utf-8')

