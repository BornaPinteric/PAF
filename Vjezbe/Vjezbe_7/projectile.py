import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self,v0,k0,m,r,C,A):
        self.vx=v0*np.cos(k0/180*np.pi)
        self.vy=v0*np.sin(k0/180*np.pi)
        self.x=0
        self.y=0
        self.m=m
        self.r=r
        self.C=C
        self.A=A
        self.ax=-r*C*A/2/m*self.vx*abs(self.vx)
        self.ay=-9.81-r*C*A/2/m*self.vy*abs(self.vy)
        self.state0=(self.vx,self.vy)
    def reset(self):
        self.vx,self.vy=self.state0
        self.x=0
        self.y=0
        self.ax=-self.r*self.C*self.A/2/self.m*self.vx*abs(self.vx)
        self.ay=-9.81-self.r*self.C*self.A/2/self.m*self.vy*abs(self.vy)
    def __moveE(self,dt):
        self.vx+=self.ax*dt
        self.x+=self.vx*dt
        self.ax=-self.r*self.C*self.A/2/self.m*self.vx*abs(self.vx)
        self.vy+=self.ay*dt
        self.y+=self.vy*dt
        self.ay=-9.81-self.r*self.C*self.A/2/self.m*self.vy*abs(self.vy)
    def plot_Euler(self,list_dt):
        for dt in list_dt:
            X=[]
            Y=[]
            X.append(self.x)
            Y.append(self.y)
            while self.y>=0:
                self.__moveE(dt)
                X.append(self.x)
                Y.append(self.y)
            self.reset()
            plt.plot(X,Y)
        plt.title("Euler")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.legend(["dt=0.1","dt=0.01","dt=0.001"], loc ="upper right")
        plt.show()
    def __moveRK(self,dt):
        k1vx=self.ax*dt
        k1x=self.vx*dt
        k2vx=-self.r*self.C*self.A/2/self.m*(self.vx+k1vx/2)*abs(self.vx+k1vx/2)*dt
        k2x=(self.vx+k1vx/2)*dt
        k3vx=-self.r*self.C*self.A/2/self.m*(self.vx+k2vx/2)*abs(self.vx+k2vx/2)*dt
        k3x=(self.vx+k2vx/2)*dt
        k4vx=-self.r*self.C*self.A/2/self.m*(self.vx+k3vx/2)*abs(self.vx+k3vx/2)*dt
        k4x=(self.vx+k3vx/2)*dt
        k1vy=self.ay*dt
        k1y=self.vy*dt
        k2vy=(-9.81-self.r*self.C*self.A/2/self.m*(self.vy+k1vy/2)*abs(self.vy+k1vy/2))*dt
        k2y=(self.vy+k1vy/2)*dt
        k3vy=(-9.81-self.r*self.C*self.A/2/self.m*(self.vy+k2vy/2)*abs(self.vy+k2vy/2))*dt
        k3y=(self.vy+k2vy/2)*dt
        k4vy=(-9.81-self.r*self.C*self.A/2/self.m*(self.vy+k3vy/2)*abs(self.vy+k3vy/2))*dt
        k4y=(self.vy+k3vy/2)*dt
        self.vx+=(k1vx+2*k2vx+2*k3vx+k4vx)/6
        self.x+=(k1x+2*k2x+2*k3x+k4x)/6
        self.vy+=(k1vy+2*k2vy+2*k3vy+k4vy)/6
        self.y+=(k1y+2*k2y+2*k3y+k4y)/6
        self.ax=-self.r*self.C*self.A/2/self.m*self.vx*abs(self.vx)
        self.ay=-9.81-self.r*self.C*self.A/2/self.m*self.vy*abs(self.vy)
    def plot_comp(self,dt):
        X1=[]
        Y1=[]
        X1.append(self.x)
        Y1.append(self.y)
        while self.y>=0:
            self.__moveE(dt)
            X1.append(self.x)
            Y1.append(self.y)
        self.reset()
        X2=[]
        Y2=[]
        X2.append(self.x)
        Y2.append(self.y)
        while self.y>=0:
            self.__moveRK(dt)
            X2.append(self.x)
            Y2.append(self.y)
        self.reset()
        plt.plot(X1,Y1)
        plt.plot(X2,Y2)
        plt.title("Comparison")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.legend(["Euler, dt="+str(dt),"Runge-Kutta, dt="+str(dt)], loc ="upper right")
        plt.show()