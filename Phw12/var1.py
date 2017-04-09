import re
def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()

    text = re.split('\.|!|\?|\?!|\.\.\.', text)
    text = [re.sub(',|"|“|”|>|<|«|»|@|&|#|\+|=|[|]|{|}|\\\|\/|\*|:|;|—|(|)|\'|\|', '', i) for i in text]

    for i in text: 
        if i == '':
            text.remove('')
        if i == ' ':
            text.remove(' ')
    return(text)


def splitwords(fname):
    text = (opentext(fname))
    text = [i.split() for i in text]
    text1 = [j for i in text for j in i]
    return(text1)

def wordlen(fname):
    text = splitwords(fname)
    arr_len = [len(i) for i in text]
    return(arr_len)

def formatting(fname):
    text = splitwords(fname)
    arr_len = wordlen(fname)
    for i in range(len(text)):
        if arr_len[i]>7:
            print(text[i] + '{:->10}'.format(arr_len[i]))

def main():
    formatting('fname.txt')

if __name__ == '__main__':
    main()
