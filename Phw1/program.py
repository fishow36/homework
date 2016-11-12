print ('Введите число а')
a = float(input())

print ('Введите число b')
b = float(input())

print ('Введите число c')
c = float(input())

if a+b == c:
    print('a и b в сумме дают c')
else:
    print('a и b в сумме не дают с')
    
if c ==  -b/a:
    print('c является решением линейного уравнения ax + b = 0')
else:
    print('c не является решением линейного уравнения ax + b = 0')

input()    
    
