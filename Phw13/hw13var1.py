import os
import shutil
import re
k = 0
reg_digits = '[0-9]'
names = os.listdir('.')
for i in names:
    print (i)
    if os.path.isdir(i) and re.search(reg_digits, i):
        k+=1
print('Папок, которые содержат цифры в названии, в данной папке ' + str(k))
