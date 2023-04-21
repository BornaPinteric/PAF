import numpy as np
import matplotlib.pyplot as plt
class HarmonicOscillator:
    def __init__(self,m,k,x0,v0):
        self.m=m
        self.k=k
        self.v=v0
        self.x=x0
        self.a=-self.k/self.m*self.x
        self.state0=(v0,x0)
    def __move(self,dt):
        self.v+=self.a*dt
        self.x+=self.v*dt
        self.a=-self.k/self.m*self.x
    def reset(self):
        self.v,self.x=self.state0
        self.a=-self.k/self.m*self.x
    def period(self,dt=0.05):
        t=0
        T=[]
        loop=True
        while loop:
            self.__move(dt)
            t+=dt
            while self.v<=0:
                self.__move(dt)
                t+=dt
                if self.v>=0:
                    T.append(t)
                    if (T[-1]-T[0])>dt:
                        loop=False
                        break     
        self.reset()
        return ((T[-1]-T[0]))
    def plot_trajectory(self,dt=0.05):
        T=np.arange(0,3*self.period(dt),dt)
        X=[]
        V=[]
        A=[]
        for t in T:
            X.append(self.x)
            V.append(self.v)
            A.append(self.a)
            self.__move(dt)
        self.reset()
        fig,ax=plt.subplots(3)
        ax[0].plot(T,X)
        ax[0].set(xlabel="t[s]",ylabel="x[m]")
        ax[1].plot(T,V)
        ax[1].set(xlabel="t[s]",ylabel="v[m/s]")
        ax[2].plot(T,A)
        ax[2].set(xlabel="t[s]",ylabel="a[m/s^2]")
        plt.show()
    def osc_err(self):
        t1=[]
        T1=self.period(0.05)
        X1=[]
        t=0
        while t<T1:
            X1.append(self.x)
            self.__move(0.05)
            t+=0.05
            t1.append(t)
        self.reset()
        t2=[]
        T2=self.period(0.01)
        X2=[]
        t=0
        while t<T2:
            X2.append(self.x)
            self.__move(0.01)
            t+=0.01
            t2.append(t)
        self.reset()
        t3=[]
        T3=self.period(0.001)
        X3=[]
        t=0
        while t<T3:
            X3.append(self.x)
            self.__move(0.001)
            t+=0.001
            t3.append(t)
        self.reset()
        plt.plot(t3,X3,".",markersize=0.5)
        plt.plot(t2,X2,".",markersize=1)
        plt.plot(t1,X1,".",markersize=2)
        plt.xlabel("t[s]")
        plt.ylabel("x[m]")
        plt.legend(["dt=0.001","dt=0.01","dt=0.05"], loc ="lower right")
        plt.show()