import os
import shutil

print(os.path.abspath('.'))
print(os.getcwd())
print(os.path.exists('645.py'))
print(os.listdir('.'))
##s = 'Hello'
##i = 1
##for f in os.listdir('.'):
##    print(f)
##    if f.endswith('43.txt'):
##        with open(f, 'a', encoding = 'utf-8') as w:
##            w.write(s*i)
##            i+=1
os.makedirs('folder1\\folder2')
