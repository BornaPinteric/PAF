import math
def aritm_sredina(X): #lista X s proizvoljnim vrijednostima
    x=sum(X)/len(X)
    s=0.0
    for xi in X:
        s+=(xi-x)**2
    s=math.sqrt(s/(len(X)*(len(X)-1)))
    return x,s #sredina i devijacija
print(aritm_sredina([10.,11.,11.]))