import numpy as np

a = np.array([[-1,2,3],[5,-6,7],[9,1,0]])
b = np.array([[0,9,1],[-5,3,1],[6,3,9]])

print(a)
print(b)

print(np.absolute(a))
print(np.absolute(b))

print(np.negative(a))
print(np.negative(b))

print(np.append(a,[[1,1,1]], axis = 0))
print(np.append(a,[[1],[1],[1]],axis = 1))

print(np.delete(a,1,0))
print(np.delete(a,1,1))

c = np.concatenate([a,b],axis = 0)
d = np.concatenate([a,b],axis = 1)

print(c)
print(d)

print(d[2,:])
print(c[:,1])
print(d[0:2,0:2])

print(np.max(a))
print(np.max(c,axis=0))
print(np.min(c,axis=0))
print(np.min(c,axis=1))

print(np.sum(a))

