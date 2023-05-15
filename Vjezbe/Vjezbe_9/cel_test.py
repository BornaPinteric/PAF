import cel_body as c
Sun=c.CelestialBody(m=1.989*(10**30),pos0=(0.,0.),v0=(0.,0.))
Earth=c.CelestialBody(m=5.9742*(10**24),pos0=(1.468*(10**11),0.),v0=(0.,29783.))
c.plot_2(Earth,Sun,T=365) #T u danima