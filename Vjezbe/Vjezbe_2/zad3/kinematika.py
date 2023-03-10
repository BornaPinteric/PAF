import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje(F,m,t0):
    a=[]
    v=[]
    x=[]
    t=[]
    a.append(F/m)
    v.append(0)
    x.append(0)
    t.append(0)
    dt=0.05
    for i in range(int(round(t0/dt))):
        a.append(a[i])
        v.append(v[i]+a[i+1]*dt)
        x.append(x[i]+v[i+1]*dt)
        t.append(t[i]+dt)
    fig,ax=plt.subplots(3,sharex=True)
    ax[0].plot(t,x)
    ax[0].set(ylabel="x")
    ax[1].plot(t,v)
    ax[1].set(ylabel="v")
    ax[2].plot(t,a)
    ax[2].set(ylabel="a", xlabel="t")
    plt.show
def kosi_hitac(v0,kut,t0):
    g=9.81
    vx=v0*np.cos(kut/180*np.pi)
    vy=v0*np.sin(kut/180*np.pi)
    x=[]
    y=[]
    t=[]
    x.append(0)
    y.append(0)
    t.append(0)
    dt=0.05
    for i in range(int(round(t0/dt))):
        vy=vy-g*dt
        x.append(x[i]+vx*dt)
        y.append(y[i]+vy*dt)
        t.append(t[i]+dt)
    fig,ax=plt.subplots(1,3)
    ax[0].plot(x,y)
    ax[0].set(ylabel="y", xlabel="x")
    ax[1].plot(t,x)
    ax[1].set(ylabel="x", xlabel="t")
    ax[2].plot(t,y)
    ax[2].set(ylabel="y", xlabel="t")
    plt.show