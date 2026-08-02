import numpy as np
#create matrix
a=np.array([[1,2],[3,4]])
b=np.array([[4,5],[4,6]])
print(a)

#shape
print(a.shape)

#matrix operations
print(a+b)
print(a-b)

#scalar multiplication
print(a*2)

#matrix multiplication
print(np.matmul(a,b))
# or
print(a@b)

#identity matrix
I=np.eye(3)
print(I)

#transpose
print(a.T)
print(b.T)

#inverse matrix
print(np.linalg.inv(a))

#determinant
print(np.linalg.det(a))