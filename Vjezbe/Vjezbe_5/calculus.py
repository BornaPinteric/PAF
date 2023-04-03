import numpy as np
def d_3(f,x,e=0.01):
    return (f(x+e)-f(x-e))/(2*e)
def d_2(f,x,e=0.01):
    return (f(x+e)-f(x))/e
def der_liste(f,x0,xn,e=0.01,metoda="",dx=0.01):
    X=[x0]
    if metoda=="":
        D=[d_3(f,x0,e)]
    else:
        D=[d_2(f,x0,e)]
    while X[-1]<=xn:
        X.append(X[-1]+dx)
        if metoda=="":
            D.append(d_3(f,X[-1],e))
        else:
            D.append(d_2(f,X[-1],e))
    return X,D
def int_p(f,x0,xn,n):
    X=np.linspace(x0,xn,n+1)
    dx=(xn-x0)/n
    I_l=0
    I_d=0
    for i in range(n):
        I_l+=dx*X[i]
        I_d+=dx*X[i+1]
    return I_l,I_d
def int_t(f,x0,xn,n):
    X=np.linspace(x0,xn,n+1)
    dx=(xn-x0)/n
    I=0
    for i in range(n):
        I+=dx*(X[i]+X[i+1])/2
    return I