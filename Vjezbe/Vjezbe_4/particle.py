import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v0,k0,x0,y0,ax=0,ay=-9.81):
        self.v=v0
        self.k=k0
        self.x=x0
        self.y=y0
        self.ax=ax
        self.ay=ay
        self.state0=(v0,k0,x0,y0)
    def printInfo(self):
        print("brzina: {}".format(self.v))
        print("kut otklona: {}".format(self.k))
        print("polozaj: ({}, {})".format(self.x,self.y))
    def reset(self):
        self.v,self.k,self.x,self.y=self.state0
    def __move(self,dt):
        vx=self.v*np.cos(self.k/180.*np.pi)+self.ax*dt
        vy=self.v*np.sin(self.k/180.*np.pi)+self.ay*dt
        self.v=np.sqrt(vx**2+vy**2)
        self.k=np.arctan(vy/vx)/np.pi*180.
        if vx<0:
            self.k+=180
        self.x+=self.v*np.cos(self.k/180.*np.pi)*dt
        self.y+=self.v*np.sin(self.k/180.*np.pi)*dt
    def range(self,dt=0.05):
        x0=self.x
        while self.y>0:
            self.__move(dt)
        R=abs(self.x-x0)
        self.reset()
        return R
    def plot_trajectory(self,dt=0.05):
        X=[]
        Y=[]
        X.append(self.x)
        Y.append(self.y)
        while self.y>0:
            self.__move(dt)
            X.append(self.x)
            Y.append(self.y)
        self.reset()
        plt.plot(X,Y)
        plt.show()