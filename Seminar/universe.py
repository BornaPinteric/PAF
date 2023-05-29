import numpy as np
import matplotlib.pyplot as plt
class Planet:
    def __init__(self,name,m,pos0,v0):
        self.name=name
        self.m=m
        self.pos=np.array(pos0)
        self.v=np.array(v0)
        self.a=(0,0)
        self.state0=(self.pos,self.v)
    def reset(self):
        self.pos,self.v=self.state0
        self.a=(0,0)
class Universe:
    def __init__(self,planets):
        self.P=planets
    def __move(self,dt): 
        G=6.67408/(10**11)
        for i in range(len(self.P)):
            self.P[i].a=(0,0)
            for j in range(len(self.P)):
                if j!=i:
                    rij=self.P[j].pos-self.P[i].pos
                    r=0.
                    for xi in rij:
                        r+=xi**2
                    r=np.sqrt(r)
                    self.P[i].a+=(G*self.P[j].m/r**3)*rij
        for p in self.P:
            p.v+=p.a*dt
            p.pos+=p.v*dt
    def simulate(self,T=365,dt=24*3600):
        Legend=[]
        for p in self.P:
            X=[]
            Y=[]
            X.append(p.pos[0])
            Y.append(p.pos[1])
            t=0
            while t<=T*24*3600:
                self.__move(dt)
                X.append(p.pos[0])
                Y.append(p.pos[1])
                t+=dt
            p.reset()
            plt.plot(X,Y)
            Legend.append(p.name)
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.title("Solar system")
        plt.legend(Legend)
        plt.show()
