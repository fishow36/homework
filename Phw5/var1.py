table = []
k = 0
i = int()
j = int()
m = int()
sumnumb = 0
with open ('newlines.txt', 'r', encoding = 'utf-8') as text:
    lines = text.readlines()

for i in range(len(lines)):
    
    for j in range(len(lines[i])):
        
        if lines[i][j] == ' ':
            k +=1
            
    table.append(k+1)
    k = 0

for i in range (len(table)):
    k += 1
    sumnumb += table[i]

sumnumb = sumnumb/k
print(sumnumb)
            
    
