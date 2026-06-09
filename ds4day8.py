import numpy
#from numpy import array
l=[1,2,3]
print(l)

arr=numpy.array(l)
print(arr)

#eg-2
import numpy
l=[[1,2,3],[2,3,4]]
print(l)

arr=numpy.array([[1,2,3],[2,3,4]])
print(arr)

print(l[1][2])
print(arr[1][2])

#replacing the element
import numpy
l=[[1,2,3],[4,5,6]]
print(l)
l[1][0]=100
print(l)


arr=numpy.array([[1,2,3],[4,5,6]])
print(arr)
arr[1][0]=100
print(arr)

#operation on list and array as numpy
l=[1,2,3]
lm=l*2
print(lm)

import numpy as np
arr=np.array(l)
arrm=arr*2
print(arrm)

#comparison
import time
start=time.time()
l=[i*2 for i in range (1000000)]
print("list op:-",time.time() - start)

import numpy as np
start=time.time()
arr = np.array(1000000)*2
print("array op:-",time.time() - start)

#zeroes array
import numpy as np
arr = np.zeros(5)#use ones for print 1
print(arr)

#2d
arr1=np.zeros((3,4))#use ones for print 1
print(arr1)


import numpy as np
arr1=np.zeros((3,4))+6
print(arr1)

arr2=np.full((3,4),1)
print(arr2)


import numpy as np
arr=np.random.random(5)
print(arr)

arr1=np.random.random((2,3))
print(arr1)


import numpy as np
arr=np.arange(5)
print(arr)


import numpy as np
arr=np.arange(1,5)
print(arr)