import numpy
import matplotlib.pyplot as plt
def unos():
    while True:
        try:
            x=float(input("x: "))
            y=float(input("y: "))
            break
        except:
            print("Niste upisali broj")
    return x,y
def pravac(t1,t2):
    k=(t2[1]-t1[1])/(t2[0]-t1[0])
    l=t1[1]-k*t1[0]
    print("y={}*x{}{}".format(str(k),("+" if l>0 else ""),(str(l) if l!=0 else "")))
    return lambda x: k*x+l
print("unos prve tocke")
t1=unos()
print("unos druge tocke")
t2=unos()
fx=pravac(t1,t2)
x=numpy.linspace(t1[0],t2[0],10)
y=fx(x)
plt.plot(x,y)
plt.plot([t1[0],t2[0]],[t1[1],t2[1]],'o')
show=(True if input("upisite \'y\' ako zelite prikazati graf a \'n\' ako ga zelite spremiti kao pdf: ")=='y' else False)
if show:
    plt.show
else:
    ime=input("ime pdfa: ")
    plt.savefig(ime+'.pdf')