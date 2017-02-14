import re

reg_lemma = r'<w.*?</w>'

reg_1f = r'type="l.f'

reg_body = r'<body>(.*?)</body'

reg_tagopen = r'<.*? '
reg_tagclose = r'</w>'

def opentextlist(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def opentextlines(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    return text


def writelen(fname):
    text = opentextlines(fname)
    with open ('result_len.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(len(text)))

def listoflemmas(fname):
    text = opentextlist(fname)
    listoflemmas = re.findall(reg_lemma, text)
    return listoflemmas


def freqdictionary(fname):
    list = listoflemmas(fname)
    freqdict = {}
    for i in range(len(list)):
        if list[i] in freqdict:
            freqdict[list[i]]+=1
        else: freqdict[list[i]] = 1
    return freqdict

def writekeys(fname):
    dict = freqdictionary(fname)
    with open ('result_keys.txt', 'w', encoding = 'utf-8') as f:
        for key in dict:
            f.write(key + '\n')

def count1f(fname):
    dict = freqdictionary(fname)
    with open ('result_count1f.txt', 'w', encoding= 'utf-8') as f:
        for key in dict:
            if re.search(reg_1f, key) != None:
                f.write(str(key) + ' - ' + str(dict[key]) + '\n')

##def subbody(fname):
##    corpora = opentextlist(fname)
##    newtext = re.search(reg_body, corpora).group(1)
##    newxtext = re.sub(reg_tag, reg_tag., newtext)
##    Не доделано
    

def filename():
    fname = input('Введите имя файла в xml: ')
    return fname


def main():
    fname = filename()
    writelen(fname)
    writekeys(fname)
    count1f(fname)

if __name__ == '__main__':
    main()

    
