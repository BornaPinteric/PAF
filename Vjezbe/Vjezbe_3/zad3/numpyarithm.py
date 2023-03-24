import numpy as np
def aritm_sredina(X):
    return np.mean(X),np.std(X)/np.sqrt(len(X)-1) #sredina i devijacija
print(aritm_sredina([10,11,10]))