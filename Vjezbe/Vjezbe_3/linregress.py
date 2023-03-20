import math
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
def modul_torzije(M,phi):
    mp=0
    m2=0
    p2=0
    for i in range(len(M)):
        mp+=M[i]*phi[i]
        m2+=M[i]**2
        p2+=phi[i]**2
    mp/=len(M)
    m2/=len(M)
    p2/=len(phi)
    D=mp/p2
    s=math.sqrt((m2/p2-D**2)/len(M))
    return D,s
print(modul_torzije(M,phi))