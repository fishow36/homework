lines = []
table_conj = []

table_n_sg_f = []
table_dict = []
ipm_sum = 0
k = 0
with open ('diction.txt', 'r', encoding = 'utf-8') as text:
    lines_text = text.readlines()

lines = lines_text
  

for i in range(len(lines)):
    lines[i] = lines[i].split('|')
    lines[i][0] = lines[i][0].rstrip()


    if lines[i][1].find('союз') != -1:
        table_conj.append(lines_text[i])    
    
    if lines[i][1].find('сущ') != -1:
        if lines[i][1].find('жен') != -1:
            if lines[i][1].find('ед') != -1:
                table_n_sg_f.append(lines[i][0])
                ipm_sum += float(lines[i][2])
print(table_conj)
print(table_n_sg_f)
print(ipm_sum)

word = input('Введите слово: ')
table_dict.append(word)
while word:
    word = input('Введите слово: ')
    table_dict.append(word)

for i in range(len(table_dict)):
    for j in range(len(lines)):
        if table_dict[i] == lines[j][0]:
            print('а)' + lines[j][1] + 'б)' + lines[j][2])
            k = 1
    if k != 1:
        print('Такого слова в словаре нет')
        k = 0

    

