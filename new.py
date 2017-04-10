import os
import shutil
m = []
print(os.path.abspath('.'))
s = input('Введите предложение без знаков препинания на английском языке: ')
m = s.split()
oldfolder = ''
print(m)

for i in m:
    os.mkdir(oldfolder + '\\' + i)
    oldfolder = oldfolder + '\\' + i

##а надо заменить пробелы на бэкслэши
