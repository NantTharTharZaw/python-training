# Virtual envirinment
# numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


python_list = [1,2,3]

print((python_list * 2))
numpy_array = np.array([1,2,3])
print(numpy_array * 2)


# vectorization
mark_list = [6,7,8]
marks_array = np.array(mark_list)
vectorized = marks_array + 5
print(vectorized)


mark_list = [6,7,8]
with_loop = []
for mark in mark_list:
    with_loop.append(mark + 5)
print(with_loop)


import numpy as np
array = np.zeros((2,3),dtype=int)
print(array.dtype)
print(array)

print(np.ones((2,3)))

# np.arrange(start,stop,step)
print(np.arange(1,10,2))

print(np.linspace(0,10,num=5))
print(np.linspace(0,10,num=5,endpoint=False))

mix_numbers = np.array([1,2,5.3,3])
mixed_text = np.array([1,"2",3])

print(mix_numbers)
print(mix_numbers.dtype)

print(mixed_text)
print(mixed_text.dtype.kind)
print(mixed_text.astype(float) + 5)

data = np.array([10,20,30,40,50],dtype=np.int64)

print(data)
print(data.itemsize)#byte
print(data.size)
print(data.nbytes)

# Dimension

a = np.array(10)
print(a)
print(a.ndim)

# 1 Dimension

a = np.array([10,20,30])
print(a)
print(a.ndim)

# 2 Dimension include row and col

b = np.array([
    [10,20,30],
    [40,50,60]
])
print(b)
print(b.ndim)
print(b.shape)

# 3 Dimension add layer

c = np.array([
    [[10,20],[30,40]], #layer0
    [[50,60],[70,80]]  #layer1
])
print(c)
print(c.ndim)
print(c.shape)

#print(c[layer,row,col]) 
print(c[1,0,1])

# slicing

numbers = np.array([10,20,30,40,50])

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::4])
print(numbers[::-1])

original = np.array([10,20,30,40])
part = original[1:3].copy()

part[0] = 999
print(part)
print(original)

numbers = np.array([10,20,30])

print(numbers + 5)
print(numbers - 5)
print(numbers * 5)
print(numbers / 5)

values = np.array([1.2,2.7,-1.2])
print(np.round(values))
print(np.floor(values))
print(np.ceil(values))

marks = np.array([60,70,80,90])

print(np.sum(marks))
print(np.mean(marks))
print(np.min(marks))
print(np.max(marks))

marks = np.array([
        [60,70,80],
        [80,90,100]
])

print(np.sum(marks))#all
print(np.sum(marks,axis=0))#col
print(np.sum(marks,axis=1))#row

# Boolean Masking
ages = np.array([15,18,22,16,30])
mask = ages < 18

print(mask)
print(ages[mask])

# Variance & Standard deviation
numbers = np.array([1,40,80,100])

print(np.mean(numbers))
print(np.var(numbers))
