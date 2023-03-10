import matplotlib.pyplot as plt
def jednoliko_gibanje(F,m):
    a=[]
    v=[]
    x=[]
    t=[]
    a.append(F/m)
    v.append(0)
    x.append(0)
    t.append(0)
    dt=0.05
    for i in range(int(round(10/dt))):
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
jednoliko_gibanje(float(input("F(N): ")),float(input("m(kg): ")))