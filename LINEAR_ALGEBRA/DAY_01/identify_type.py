import numpy as np
items=[25,np.array([1,2]),np.array([4]),np.array([170,90,76])]
for i in items:
    if isinstance(i,(int,float)):
        print("Scalar->",i)
    elif isinstance(i,np.ndarray)and i.ndim==1:
        print("Vector->",i)