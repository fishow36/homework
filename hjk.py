import re
regurl = r'<a\s+href="(.*?)".*?>(.*?)</a>'

def opentext(fname):
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def findurl(fname):
    text = opentext(fname)
    newlist = re.findall(regurl, text)
    return newlist

mas = findurl('Africa.html')
for link in mas[:20]:
    print(link[1], '    ', link[0])
    
