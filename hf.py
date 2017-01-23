d = {}  ## create a dictionary - неупорядоченные
        ## Элис(ключ: строка или число): 2323 (значение)

d = { "Alice": '1232',
  'Bob': '432' }

print (d['Bob'])

d['Bob'] = '999'  ## изменить значение
d['Tom'] = '9043' ## добавить новый ключ

print(len(d))  ## сколько ключей в словаре

if 'Bob' in d:           ## если в словаре есть Боб
    print (d['Bob'])

for key in d:
    print(key + '$' + d[key])

d.keys()  ## массив ключей
d.values() ##  массив значений

if '999' in d.values():
    print('yes')

d.keys.sort()  ## рассортировать массив по алфавиту
print(d.keys)
