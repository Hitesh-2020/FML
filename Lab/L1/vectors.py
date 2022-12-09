import numpy as np

a = np.random.randint(10, size=[3,1])
b = np.random.randint(10, size=[1,3])

print(a+b)
print(np.add(a,b))

print(a-b)
print(np.subtract(a,b))

print(a*b)
print(np.multiply(a,b))

print(a@b)
print(np.matmul(a,b))

#Indexing
print(a[1])
print(a[0:2])
print(a[:])