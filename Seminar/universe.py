import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as ani
class Planet:
    def __init__(self,name,m,pos0,v0):
        self.name=name
        self.m=m
        self.pos=np.array(pos0)
        self.v=np.array(v0)
        self.a=(0,0)
        self.state0=(pos0,v0)
    def reset(self):
        self.pos=np.array(self.state0[0])
        self.v=np.array(self.state0[1])
        self.a=(0,0)
class Universe:
    def __init__(self,planets):
        self.P=planets
    def resetall(self):
        for p in self.P:
            p.reset()
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
        fig,ax=plt.subplots(1)
        ax.set_aspect("equal")
        Legend=[]
        for p in self.P:
            self.resetall()
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
            ax.plot(X,Y)
            Legend.append(p.name)
        ax.set_xlabel("x[m]")
        ax.set_ylabel("y[m]")
        ax.set_title("Solar system")
        ax.legend(Legend)
        self.resetall()
        point,=ax.plot(0,0,'ko',markersize=12)
        def animation_function(i):
            x=[]
            y=[]
            for p in self.P:
                x.append(p.pos[0])
                y.append(p.pos[1])
            point.set_xdata(x)
            point.set_ydata(y)
            self.__move(dt)
            return point,
        animation=ani(fig,func=animation_function,frames=np.arange(0,T*24*3600+1,dt),interval=1,repeat=False)
        plt.show()
