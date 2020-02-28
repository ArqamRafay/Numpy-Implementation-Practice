import numpy as np

# Creating Array
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)], dtype=int)
# print(b)

# initial Placeholders
# 1D array of alll zerros
c = np.zeros(3)
#  2D array of all zerros
d = np.zeros((2, 3))
# 3x4 array of random floats betweeen 0-1
f = np.random.rand(3, 5)
# 4x4 array of 0 with 1 on digonal 
e= np.eye(4)
# print(e)

# saving and loading
# np.save("newarray",x)


# Operator
#  copy array a in array z (Replica)
z = np.copy(a) 
v = a.sort()
m  = np.append(z, 9)
n  = np.insert(z, 9,2)
print (n)



# Genrerate random number 
# make string encripted
