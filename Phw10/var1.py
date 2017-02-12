import re

reg_infobox = '<table class="infobox">(.|\n)+?</table>((.|\n)+?)</table>'  ## Перенос строки - не любой символ?..
reg_capital = 'Столица((.|\n)+?)<span style="display: none; speak: none;">((.)+?)</span>'  ## Как по-другому?..
def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return(text)

def findcapital(fname):
    text = opentext('Germany.html')
    if re.search(reg_infobox, text):
        infobox = re.search(reg_infobox, text).group(2)
        
        if re.search(reg_capital, infobox):
            result = re.search(reg_capital, infobox).group(3)

        else:
            result = 'Capital not found'
            
    else:
        result = 'infobox not found'
    return result

def filename():
    fname = input('Введите имя файла: ')
    return fname

def writeresult(result):
    with open('Capital.txt', 'w', encoding = 'utf-8') as f:
        f.write('Столица - ' + result)


def main():
    fname = filename()
    result = findcapital(fname)
    writeresult(result)

if __name__ == '__main__':
    main()



