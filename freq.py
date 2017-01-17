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

def freqlist(fname):
    freqdict = {}
    for i in range(len(text)):
        if text[i] in freqdict:
            freqdict[i] +=1
        else:
            freqdict[i] = 1
    return freqdict

print(freqlist('fname.txt'))
