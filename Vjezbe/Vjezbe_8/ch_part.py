import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
class ChargedParticle:
    def __init__(self,v0,q,m):
        self.v=np.array(v0)
        self.pos=(0,0,0)
        self.q=q
        self.m=m
        self.state0=v0
    def reset(self):
        self.v=np.array(self.state0)
        self.pos=(0,0,0)
    def __move(self,E,B,dt):
        a=self.q/self.m*(E+np.cross(self.v,B))
        self.v=self.v+a*dt
        self.pos=self.pos+self.v*dt
    def plot_tr(self,E,B,dt=0.01):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1,projection="3d")
        T=0
        POS=[]
        POS.append((0,0,0))
        while T<50:
            self.__move(E,B,dt)
            POS.append(self.pos)
            T+=dt
        self.reset()
        ax.plot3D([p[0] for p in POS],[p[1] for p in POS],[p[2] for p in POS],label="Charged particle")
        self.q*=(-1)
        T=0
        POS=[]
        POS.append((0,0,0))
        v0=self.v
        while T<50:
            self.__move(E,B,dt)
            POS.append(self.pos)
            T+=dt
        self.reset()
        ax.plot3D([p[0] for p in POS],[p[1] for p in POS],[p[2] for p in POS],label="Charged particle (opposite charge)")
        ax.set_xlabel("x[m]")
        ax.set_ylabel("y[m]")
        ax.set_zlabel("z[m]")
        plt.legend()
        plt.show()