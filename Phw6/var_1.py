import random

def punct():
    with open('punct.txt','r', encoding = 'utf-8') as m:
        punct = m.read().split('\n')      
    return random.choice(punct)


def adj():
    with open('adject.txt','r', encoding = 'utf-8') as m:
        adjectives = m.read().split('\n')      
    return random.choice(adjectives)

def nounf2():
    with open('nouns_f_2.txt','r', encoding = 'utf-8') as m:
        nounf2 = m.read().split('\n')      
    return random.choice(nounf2)

def imperative():
    with open('imper.txt','r', encoding = 'utf-8') as m:
        imperative = m.read().split('\n')      
    return random.choice(imperative)

def adj_ins_f():
    with open('adj_ins_f.txt','r', encoding = 'utf-8') as m:
        adj_ins_f = m.read().split('\n')      
    return random.choice(adj_ins_f)

def nouns_f_3_ins():
    with open('nouns_f_3_ins.txt','r', encoding = 'utf-8') as m:
        nouns_f_3_ins = m.read().split('\n')      
    return random.choice(nouns_f_3_ins)

def conj_1():
    with open('conj_1.txt','r', encoding = 'utf-8') as m:
        conj_1 = m.read().split('\n')      
    return random.choice(conj_1)

def verb_3sg_fut():
    with open('verb_3sg_fut.txt','r', encoding = 'utf-8') as m:
        verb_3sg_fut = m.read().split('\n')      
    return random.choice(verb_3sg_fut)

def nouns_mfn_2():
    with open('nouns_mfn_2.txt','r', encoding = 'utf-8') as m:
        nouns_mfn_2 = m.read().split('\n')      
    return random.choice(nouns_mfn_2)

def line1():
    return adj() + ' ' + nounf2() + punct()
def line2():
    return imperative() + ' ' + adj_ins_f() + ' ' + nouns_f_3_ins() + punct()

def line3():
    return conj_1() + ' ' + verb_3sg_fut() + ' ' + nouns_mfn_2() + punct()



print(line1())
print(line2())
print(line3())
