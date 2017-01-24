import re


with open ('fname.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    
regtravka = r"\b[Тт]рав(к((а|и|е|у)|а(х|ми?))|о[кй])\b"

if re.search(regtravka,text)!= None:
    print("да, есть")
