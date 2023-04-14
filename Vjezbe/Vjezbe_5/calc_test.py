import calculus as calc
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(3,1)
xlist=np.arange(-3,3,0.01)
kubna=lambda x:x**3
kubder=lambda x:3*x**2
axs[0].plot(xlist,kubder(xlist))
axs[0].plot(calc.der_liste(kubna,-3,3)[0],calc.der_liste(kubna,-3,3)[1],"r--")
axs[0].plot(calc.der_liste(kubna,-3,3,metoda="2step")[0],calc.der_liste(kubna,-3,3,metoda="2step")[1],"y:")
axs[0].set(ylabel="d(x^3)/dx")
axs[0].set(xlabel="x")
sin=lambda x:np.sin(x)
sinder=lambda x:np.cos(x)
axs[1].plot(xlist,sinder(xlist))
axs[1].plot(calc.der_liste(sin,-3,3)[0],calc.der_liste(sin,-3,3)[1],"r--")
axs[1].plot(calc.der_liste(sin,-3,3,metoda="2step")[0],calc.der_liste(sin,-3,3,metoda="2step")[1],"y:")
axs[1].set(xlabel="x")
axs[1].set(ylabel="d(sin(x))/dx")
nlist=range(50,1001,50)
iL=[]
iD=[]
iT=[]
for n in nlist:
    iL.append(calc.int_p(kubna,0.,1.,n)[0])
    iD.append(calc.int_p(kubna,0.,1.,n)[1])
    iT.append(calc.int_t(kubna,0.,1.,n))
#int od 0 do 1 x^3 = 1/4
axs[2].plot(nlist,[0.25]*len(nlist))
axs[2].plot(nlist,iL,"r.")
axs[2].plot(nlist,iD,"g.")
axs[2].plot(nlist,iT,"y.")
axs[2].set(xlabel="N steps")
axs[2].set(ylabel="int")
plt.show()