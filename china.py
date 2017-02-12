## находить названия китайских космических аппаратов
import re

reg = '«[а-я]+-[0-9]+»'

def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = text.lower()
    return(text)

def names(fname):
    text = opentext(fname)
    res = re.findall(reg, text)
    return res


fname = input('Введите название файла: ')
print(names(fname))
