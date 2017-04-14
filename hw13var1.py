import os
import shutil
import re
def folderdigits():
    k = 0
    reg_digits = '[0-9]'
    names = os.listdir('.')
    for i in names:
        if os.path.isdir(i) and re.search(reg_digits, i):
            k+=1
    print('Папок, которые содержат цифры в названии, в данной папке ' + str(k))
def printnames():
    print('Файлы и папки, которые содержатся в данной папке: ')
    reg_name = r'.*\.'
    names = os.listdir('.')
    names_mentioned = []
    for i in names:
        if re.search(reg_name, i):
            filename = re.search(reg_name, i).group(0).strip('.')
            if filename not in names_mentioned:
                names_mentioned.append(filename)
                print(filename)


def main():
    folderdigits()
    printnames()


if __name__ == '__main__':
    main()
