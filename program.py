##
##    5 баллов - открыть файл, посчитать в нем количество слов. Распечатать это количество.
##    8 баллов - создать частотный словарь для всех слофоворм, встретившихся в тексте.
##       Распечатать его в отдельный csv-файл, отсортировав по алфавиту (на каждой строчке слово + запятая + количество вхождений).
##    10 баллов - найти все вхождения конструкции род. падеж прилагательного c безударн. окончанием -аго + род. падеж сущ. 1 или 2 скл.
##       (например, великорусскаго языка) в файле. Выписать в отдельный файл найденные конструкции и их контексты - 3 слова слева и 3 слова справа
##       (каждая конструкция и её контекст на отдельной строчке).

import re

reg_construction = r'([А-Яа-яѢѣ]+\s){3}([А-Яа-яѢѣ]+аго\s[А-Яа-яѢѣ]+[ыиая])(\s[А-Яа-яѢѣ]+){3}'

def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = text.lower()
    text = text.split()
    newtext = []
 
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,>«»@&#+=[]{}\|/<*!:;—()-?')
        if text[i] != '' and text[i] != ' ':
            newtext.append(text[i])
    return newtext

def freqdictionary(fname):
    text = opentext(fname)
    freqdict = {}
    for i in range(len(text)):
        if text[i] in freqdict:
            freqdict[text[i]]+=1
        else: freqdict[text[i]] = 1
    return freqdict

def find_construction(fname):
    text = opentext(fname)
    constructions = re.findall(reg_construction, text)
    return constructions

text = opentext('text1.txt')
print(len(text))
constr = find_construction('text1.txt')
print(constr)
                           
