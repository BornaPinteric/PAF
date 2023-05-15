import numpy as np
import matplotlib.pyplot as plt
class CelestialBody:
    def __init__(self,m,pos0,v0):
        self.m=m
        self.pos=np.array(pos0)
        self.v=np.array(v0)
        self.state0=(self.pos,self.v)
    def reset(self):
        self.pos,self.v=self.state0
def __move(b1,b2,dt):
    G=6.67408/(10**11)
    r12=b1.pos-b2.pos
    r=0.
    for xi in r12:
        r+=xi**2
    r=np.sqrt(r)
    b1.a=(-G*b2.m/r**3)*r12
    b2.a=(G*b1.m/r**3)*r12
    b1.v+=b1.a*dt
    b2.v+=b2.a*dt
    b1.pos+=b1.v*dt
    b2.pos+=b2.v*dt
def plot_2(b1,b2,T=365,dt=24*3600):
    X1=[]
    Y1=[]
    X2=[]
    Y2=[]
    t=0
    while t<=T*24*3600:
        __move(b1,b2,dt)
        X1.append(b1.pos[0])
        Y1.append(b1.pos[1])
        X2.append(b2.pos[0])
        Y2.append(b2.pos[1])
        t+=dt
    b1.reset()
    b2.reset()
    plt.plot(X1,Y1)
    plt.plot(X2,Y2)
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.title("Sun-Earth system")
    plt.legend(["Earth","Sun"])
    plt.show()