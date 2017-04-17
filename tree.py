import os

def pathdepth(path):
    k = ''
    array_tree = []
    for root, dirs, files in os.walk(path, topdown = False):
        for d in dirs:
            for f in files:
                k = len(os.path.join(d, f).split('\\')) ## глубина папки
    return(k)

def drawtree(path):
    
            

print(drawtree(r'C:\Users\student\Desktop'))
