import numpy as np
num=[15,np.array([15]),np.array([[15]]),np.array([2,5,8])]
for n in num:
    if isinstance(n,(int,float)):
        print("Scalar:",n)
    elif isinstance(n,np.ndarray):
        if n.ndim==1:
            print("Vector:",n)
        elif n.ndim==2:
            print("Matrix:",n)
            