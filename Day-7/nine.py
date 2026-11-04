# DDOF = 1 ,Sample

import numpy as np
marks = np.array([49,50,51])

print(np.mean(marks))
print(np.var(marks,ddof=1))
print(np.std(marks,ddof=1))

# DDOF = 0 ,population

import numpy as np
marks = np.array([49,50,51])

print(np.mean(marks))
print(np.var(marks,ddof=0))
print(np.std(marks,ddof=0))

# Reshape & Flatten

import numpy as np

numbers = np.array([10,20,30,40,50,60])
table = numbers.reshape(2,3) 

print(table)
# print(numbers.shape)

import numpy as np
numbers = np.array([[10,20,30],[40,50,60]])

print(numbers.reshape(2,-1))
print(numbers.reshape(3,-1))

import numpy as np
numbers = np.array([[10,20,30],[40,50,60]])

a = numbers.reshape(-1)
b = numbers.ravel()
c = numbers.flatten()

a[0] = 99

print(a)
print(b)
print(c)

# Transponse

import numpy as np
numbers = np.array([[1,2,3],[4,5,6]])

print(numbers.T)
# print(numbers.T.shape)

# Broadcasting

import numpy as np
numbers = np.array([[1,2,3],[4,5,6]])
data = np.array([1,2,3])

print(numbers + data)
print(numbers.shape)
print(data.shape)


# Scalar
numbers = np.array([1,2,3])
print(numbers + 10)

# Joining & Splitting

a = np.array([[1,2],
              [3,4]
         ] )

b = np.array([[1,2]])

print(np.concatenate((a,b),axis = 0))

l = np.array([[1,2],
              [3,4]
         ] )
r = np.array([[1],[2]])

print(np.concatenate((l,r),axis = 1))

# stack

a = np.array([[1,2]])
b = np.array([[3,4]])


