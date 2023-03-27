import numpy as np
class Particle:
    def __init__(self,v0,k0,x0,y0):
        self.v=v0
        self.k=k0
        self.x=x0
        self.y=y0
    def printInfo(self):
        print("brzina: ",self.v)
        print("kut otklona: ",self.k)
        print("polozaj: (",self.x,", ",self.y,")")
    def reset(self):
        pass
    def __move(self,dt,ax,ay):
        vx=self.v*np.cos(self.k/180*np.pi)
        vy=self.v*np.sin(self.k/180*np.pi)