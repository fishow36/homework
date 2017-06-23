import re
import os

reg_title = '<title>(.*?)</title>'
reg_author = 'content="(.*?)" name="author"'
reg_topic = 'content="(.*?)" name="topic"'
reg_loc = ''
reg_word = '</ana>(.*)'
def count_se():
    for i in (os.listdir('news')):
        with open(os.path.join('news', i), 'r') as f:
            text = f.read()
            with open ('task1.txt', 'a', encoding = 'utf-8') as m:
                m.write(i + '\t' + str(len(re.findall('<se>', text))) + '\n')

                
def make_table():
    with open ('task2.csv', 'a', encoding = 'utf-8') as m:
        m.write('Название файла' + '\t' + 'Автор' + '\t' +'Тематика текста' + '\n')
        for i in (os.listdir('news')):
            with open(os.path.join('news', i), 'r') as f:
                text = f.read()
                m.write(i + '\t' +  re.search(reg_author, text).group(1) + '\t' + re.search(reg_topic, text).group(1) + '\n')

def bigrams():
    for i in (os.listdir('news')):
        with open(os.path.join('news', i), 'r') as f:
            text = f.read()
            newtext = re.findall('<w>(.*?)</w>', text)
            for i in range(len(newtext)-1):
                if re.search('PR', newtext[i]):
                    if re.search('loc', newtext[i+1]) and re.search('S', newtext[i+1]):
                        with open ('task3.txt', 'a', encoding = 'utf-8') as m:
                            m.write(str(re.search(reg_word, newtext[i]).group(1)) + ' ' + str(re.search(reg_word, newtext[i+1]).group(1)) + '\n' )
            


def main():
    count_se()
    make_table()
    bigrams()
        

if __name__ == '__main__':
    main()


