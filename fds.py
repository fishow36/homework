import os
import re
def createdict(path):
    wordforms_dict = {}
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.txt'):
                with open (root + '\\' + f, 'r', encoding = 'utf-8') as p:
                    text = p.split()
                    for i in text:
                        word = word.strip('.,!?:;()\'\"').lower()
                        if word in wordforms_dict:
                            wordforms_dict[word] +=1
                        else:
                            wordforms_dict[word] = 1
    return wordforms_dict

print(createdict(r'C:\Users\student\Desktop\direct'))
                        
                
