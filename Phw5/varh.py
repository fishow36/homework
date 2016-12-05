table = []
k = 0
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
    
    sumnumb += table[i]

sumnumb = sumnumb/len(lines)
print(sumnumb)
            
    
