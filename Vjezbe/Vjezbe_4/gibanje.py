import particle as prt
import numpy as np
p1=prt.Particle(50,20,2,2)
#y0+v0t+1/2gt2=0
v0=p1.v*np.sin(p1.k/180.*np.pi)
t=(-v0-np.sqrt(v0**2-2*p1.ay*p1.y))/p1.ay
d=p1.v*np.cos(p1.k/180.*np.pi)*t
x=abs(d-p1.range())
print("numericki domet: {}".format(p1.range()))
print("analiticki domet: {}".format(d))
print("pogreska: {}".format(x))