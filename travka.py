import re

regtravka = r"\bтрав(к((а|и|е|у)|а(х|ми?))|о[кй])\b"
worduser = input('Введите слово: ')
while worduser:
    
    if re.search(regtravka,worduser)!= None:
        print("да, это форма слова травка")
    else:
        print("Нет, это не форма слова травка")
    worduser = input('Введите слово: ')
