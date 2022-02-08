#T1

#exercice 1 (programme 19)

def doublon(t):
    s = set()
    for i in range(len(t)):
        s.add(t[i])
    return len(s) != len(t)
        
    

#exercice 2 (programme 20)
    
def occurence(t):
    d = {}
    for x in t:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    return d


#exercice 174
from random import*


def paradoxe():
    for i in range(1000):
        a = randint(1, 365)
        
        
         
    
    
    