# split, array_split

import numpy as np

data = np.array([10,20,30,40,50,60])
for part in np.split(data,3):
    print(part) # equal

for part in np.array_split(data,5):
    print(part) # not equal
    
import numpy as np

data = np.array([
    [10,20,30,40,50,60],
    [70,80,90,100,110,120], 
])

for part in np.split(data,2,axis=0):
   print(part)
   
for part in np.split(data,2,axis=1):
   print(part)
   
for part in np.array_split(data,5,axis=0):
    print(part)
    
for part in np.array_split(data,5,axis=1):
    print(part)  
    
    
# sorting

import numpy as np

marks = np.array([49,55,51])
print(np.sort(marks)) # big to small
print(np.sort(marks)[::-1]) #small to big


# argsort

import numpy as np

names = np.array(["aye","thar","su"])
marks = np.array([49,55,51])

order = np.argsort(marks)
order = np.argsort(marks)[::-1]
print(order)


import numpy as np

marks = np.array([49,55,51])
print(np.min(marks))
print(np.argmin(marks))

print(np.max(marks))
print(np.argmax(marks))

import numpy as np

marks = np.array(["a","b","c"])
values,counts = np.unique(marks,return_counts=True)
print(values)
print(counts)

import numpy as np

marks = np.array([49,55,51])
result = np.where(marks >=50,"pass","fail")

print(result)

import numpy as np

marks = np.array([49,55,51])
passed = marks >= 50

print(passed)
print(np.any(passed)) # or gate
print(np.all(passed)) #and gate
print(np.count_nonzero(passed))

import numpy as np

marks = np.array([49,np.nan,51],dtype=float)
na = np.isnan(marks)

print(na)
print(np.count_nonzero(na))
print(marks[np.isnan(marks)])
print(marks[~np.isnan(marks)])

import numpy as np

marks = np.array([59,np.nan,51],dtype=float)
print(np.mean(marks))
print(np.nanmean(marks))

# Medium
import numpy as np

marks = np.array([59,60,70,51])
print(np.mean(marks))
print(np.median(marks))

import numpy as np

marks = np.array([10,20,30,40,50])
print(np.percentile(marks,[1,50,100]))

import numpy as np
rng = np.random.default_rng(42)
marks = rng.integers(0,101,size=(4,3))

print(marks)
print(marks.shape)


import numpy as np
rng = np.random.default_rng(42)
values = np.array(["aye","su","thar"])
chosen = rng.choice(names,size=2,replace=False)

# print(values)
# print(values.shape)
# print(np.all((values >= 0 ) & (values < 1)))
print(chosen)
print(chosen.size)
print(np.unique(chosen).size)

# Fancy Indexing
import numpy as np

marks = np.array([10,20,30,40,50])

print(marks[1])
print(marks[0:2])
print(marks[[0,2,4]])

import numpy as np

marks = np.full((2,3),5000)

print(marks)
