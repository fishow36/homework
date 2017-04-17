os.listdir('..') папка на уровень выше
os.walk('.')
tree = os.walk('.') возвращает generator object - массив, который можно увидеть только из цикла
В нём каждый элемент состоит из 3 подэлементов: рут (путь к текущей папке), папки, которые лежат в текущей папке и файлы, которые лежат там
можно идти снизу вверх: os.walk('.', topdown = False)
for root, dirs, files in os.walk('.'):
    print(root) - печатает пути ко всем папкам
    files = [f for f in files if len(f)>7]
    print(root, len(files)) напечатать сколько файлов в какой папке

os.path.join(root, f) полное название файла

whole_corpus +=text.read
с точки начинаются скрытые папки!
