import re
def search():
    with open('dino.html', 'r', encoding = 'utf-8') as f:
        page = f.read()
        query = r'\b[Дд]инозавр[а-я]{,3}\b'
        text = re.sub('<.*?>', '', page, flags = re.DOTALL)
        res = re.findall(query, text) ##ищем все формы слова динозавр
        textnorm = re.sub('(\n){2,}', '\n', text) #убираем пустоты внутри текста
        print(textnorm)
search()
