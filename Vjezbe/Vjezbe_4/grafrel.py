import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1=prt.Particle(10,60,0,0)
gr=[]
v0=p1.v*np.cos(p1.k/180.*np.pi)
t=(-v0-np.sqrt(v0**2-2*p1.ay*p1.y))/p1.ay
d=v0*t
for dt in np.linspace(0.01,0.1,100):
    gr.append(abs(d-p1.range(dt))/d*100)
plt.plot(np.linspace(0.01,0.1,100),gr)
plt.show()