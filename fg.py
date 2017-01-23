def Capital():
    countryname = input('Введите название страны: ')
    if countryname in countries:
        return print (countries[countryname])
    else:
        print('Не знаю :(')
    
def revert(countries):
    capitals = {}
    for key in countries:
        capitals[countries[key]] = key
    return capitals

def delete_doubles(countries):
    newdict = {}
    alreadyseen = []
    for key in countries:
        for i in alreadyseen:
            if countries[key] == i:
                

            else:
                alreadyseen.append(countries[key])
                
    
            


            

countries = {
    'Russia': 'Moscow',
    'Finland': 'Helsinki',
    'Italy': 'Rome',
    'Belarus': 'Minsk',
    'Spain': 'Minsk'}

##for key in countries:
##    print (key + ' - ' + countries[key])

print(delete_doubles(countries))


##Capital()


print(delete_doubles(countries))
