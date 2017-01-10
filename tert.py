
def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = text.lower()
    text = text.split()
 
    for i in range(len(text)): 
        text[i] = text[i].strip('.,*!()-?')
    text.remove('')
    return(text)


def first_letter(letter, fname):
    letter_arr = []
    text = opentext(fname)
    for i in range(len(text)):
        
        if text[i][0] == letter:
            letter_arr.append(text[i])
            
    return(letter_arr)



def questions():
    fname = input('Введите имя файла: ')
    letter = input('Введите букву: ')
    return print(first_letter(letter, fname))


def adjectives(fname):
    text = opentext(fname)
    for i in range(len(text)):
        if text[i].endswith('ая') or text[i].endswith('ой') or text[i].endswith('яя') or text[i].endswith('ое') or text[i].endswith('ий') or text[i].endswith('ее'):
            print(text[i] + ' ' + text[i+1])
            
print(opentext('fname.txt'))

adjectives('fname.txt')
    
    

