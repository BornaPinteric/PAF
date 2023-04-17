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
    def period_err(self):
        gr=[]
        T=2*np.pi*np.sqrt(self.m/self.k)
        for dt in np.linspace(0.01,0.1,500):
            gr.append(abs(T-self.period(dt))/T*100)
        plt.plot(np.linspace(0.01,0.1,500),gr)
        plt.xlabel("dt[s]")
        plt.ylabel("err[%]")
        plt.show()