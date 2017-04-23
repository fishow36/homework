import os
import re

def pathdepth(path):
    m = ''
    for root, dirs, files in os.walk(path, topdown = False):
        for d in dirs:
            k = os.path.join(root, d)
            if len(re.findall(r'\\', k))>len(re.findall(r'\\', m)):
                m = k
    m = m.replace(path, '')
    depth = len(re.findall(r'\\', m))
    return(depth)
            
def main():
    path = input('Введите путь к папке: ')
    print('Максимальная глубина папки в этом дереве: '+ str(pathdepth(path)))

if __name__ == '__main__':
    main()

