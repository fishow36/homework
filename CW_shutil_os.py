работа с файлами и папками

модуль os и shutil

Windows: C:\\users\\student\\Downloads - обычно обратный слэш, но надо экранировать
Linux, Mac: /home/student/downloads

os.path.abspath('.') - абсолютный путь к папке, в которой лежит прога (текущая)
os.getcwd() - то же самое

os.path.join(foldername, filename) - соединяет название папки и файла

os.path.exists('texts') - существует ли файл texts?

os.listdir('.') - что лежит в текущей папке?

for f in os.listdir('.'):
    print(f)

os.mkdir('folder1')) - создать папку
os.makedirs('folder1\\folder2') папка 2 в папке 1
os.rename('itwasfolder', 'nowitsvolk') - переименовать папку или файл

os.path.isfile('texts') - является ли texts файлом?
os.path.isdir('texts') - является ли texts папкой?

shutil.copy('texts\\corpus1.txt', 'texts_new\\corpus1.txt') переместить из texts в text_new
shutil.copytree('texts', 'texts_new') переместить всё, что в папке texts в папку texts_new
shutil.move('otkuda', 'kuda')

os.remove('folder\\file.txt') удалить файл
shutil.rmtree('folder') удалить папку
