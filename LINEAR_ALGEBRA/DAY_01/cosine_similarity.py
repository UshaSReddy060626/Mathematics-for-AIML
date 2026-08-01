#cosine similarity
import numpy as np
a=np.array([1,2,3])
b=np.array([3,4,5])
dot=np.dot(a,b)
norm_a=np.linalg.norm(a)
norm_b=np.linalg.norm(b)
cosine=dot/(norm_a*norm_b)
print("Cosine Similarity",cosine)