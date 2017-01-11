
def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = text.lower()
    text = text.split()
 
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,>«»@&#+=[]{}\|/<*!:;—()-?')
        if text[i] == ' ':
            text.remove('')
    return(text)

def ing_number(fname):
    k = 0
    text = opentext(fname)
    for i in range(len(text)):
        if text[i].endswith('ing'):
            k +=1
    return k


def ing_user(fname, ing_form):
    k = 0
    
    text = opentext(fname)
    for i in range(len(text)):
        if text[i] == ing_form:
            k +=1
    return k

def print_ing():
    fname = input('Введите название файла: ')
    ing_form = input('Введите необходимую форму на -ing: ')
    print('Количество слоформ на -ing в тексте: ' + str(ing_number(fname)))
    print('Количество слова ' + ing_form + ': ' + str(ing_user(fname, ing_form)))

print_ing()




    
