import re
regopen = r'\bоткр(о((ют?)|е(шь|м|т)|[йе](те)?)|ы((ть|л([аыои]?)|вш(и([хмйе]?|ми)|е(го|му?|е|й)|ая|[уе]ю)?)|в|т(ы(й|ми?|х|е)?|о((му?)|го|й|е|ю)?|ая?|ую)?))(с[ья])?\b'

def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = text.lower()
    text = text.split()
 
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,>«»@&#+=[]{}\\|/<*!:;—()\'-?')
        if text[i] == ' ':
            text.remove('')
    return(text)

def forms(fname):
    text = opentext(fname)
    alreadyseen = []
    for i in range(len(text)):

        if re.search(regopen,text[i])!= None:
            if text[i] not in alreadyseen:
                alreadyseen.append(text[i])
                    
    return alreadyseen


fname = input('Введите название файла: ')
print(opentext(fname))
print(forms(fname))
                    
