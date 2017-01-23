mydictionary = {}

def dictionary():
    with open('dictionary1.csv', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    for i in range(len(text)):
        line = text[i].split(';')
        mydictionary[line[0]] = line[1].strip('\n')
    return(mydictionary)


def riddle():
    
    mydictionary = dictionary()
    for key in mydictionary:
        i = 0
        print(key + '...')
        while i < len(mydictionary[key]):
            guess = input('Продолжите словосочетание: ')
            if guess == mydictionary[key]:
                print ('Правильно!')
                break
            else:
                print('Неправильно, попробуйте ещё раз ')
                i+=1

            if i == len(mydictionary[key]):
                print('К сожалению, попытки закончились')
            
riddle()

 
