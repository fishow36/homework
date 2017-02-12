import re

reg_mosquito = r'\b(комар)((а((ми?)|х)?)|о[мв]|у|е|ы)?\b'
reg_mosquito_cap = '(Комар)((а((ми?)|х)?)|о[мв]|у|е|ы)?'

def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return(text)

def change_mosquito(fname):
    text = opentext(fname)
    r = re.search(reg_mosquito, text)
    if r:
        text = re.sub(r.group(1), 'слон', text)
    r = re.search(reg_mosquito_cap, text)
    if r:
        text = re.sub(r.group(1), 'Слон', text)
    return text

def filename():
    fname = input('Введите имя файла: ')
    return fname

def writeresult(fname):
    text = change_mosquito(fname)
    with open('Слон.html', 'w', encoding = 'utf-8') as f:
        f.write(text)

def main():
    fname = filename()
    writeresult(fname)

if __name__ == '__main__':
    main()

