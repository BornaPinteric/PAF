import universe as u
Planet1=u.Planet(name="Sun",m=1.989*(10**30),pos0=(0.,0.),v0=(0.,0.))
Planet2=u.Planet(name="Mercury",m=3.301*(10**23),pos0=(5.79*(10**10),0.),v0=(0.,47362.))
Planet3=u.Planet(name="Venus",m=4.8673*(10**24),pos0=(1.082*(10**11),0.),v0=(0.,35021.))
Planet4=u.Planet(name="Earth",m=5.9742*(10**24),pos0=(1.468*(10**11),0.),v0=(0.,29783.))
Planet5=u.Planet(name="Mars",m=6.4169*(10**23),pos0=(2.279*(10**11),0.),v0=(0.,24077.))
Universe1=u.Universe([Planet1,Planet2,Planet3,Planet4,Planet5])
Universe1.simulate(T=5*365)