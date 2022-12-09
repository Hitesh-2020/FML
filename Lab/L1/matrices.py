import numpy as np

p = np.random.randint(10, size = [3,3])
q = np.random.randint(10, size = [3,3])

print(p+q)
print(np.add(p,q))

print(p-q)
print(np.subtract(p,q))

print(p*q)
print(np.multiply(p,q))

print(p@q)
print(np.matmul(p,q))

#Indexing
print(p[2])
print(p[0:2])
print(p[1:3,1:3])
print(np.concatenate([p,q],))
print(np.concatenate([p,q],axis=1))