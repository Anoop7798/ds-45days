#sorting
import numpy as np
arr =np.array([10,20,30,60,90,7,5])
print(arr)
arr_s=np.sort(arr)
print(arr_s)
#2d
import numpy as np
arr=np.array([[52,6,120],[2,20,42]])
print(arr)
arr_s=np.sort(arr)#by default row wise
arr_s1=np.sort(arr,axis=1)#row wise
arr_s0=np.sort(arr,axis=0)#column wise
print(arr_s1)#default short rows for column we can use axis =0& 1 for the rows
print(arr_s0)
#for dec order
arr_desc=np.sort(arr)[:,::-1]
print(arr_desc)

#filter
import numpy as np
arr=np.array([10,20,30,4,5,67,56,7,78])
print(arr)
arr_f=arr[arr>10]
print(arr_f)
arreven = arr[arr%2==0]
print(arreven)


#fancy indexing vs np.where()
import numpy as np
arr=np.array([10,20,30,4,5,67,56,7,78])
print(arr)
aar_f=arr[[0,2,4,6]]#print these index value
print(aar_f)

#np.where
import numpy as np
arr=np.array([10,20,30,4,5,67,56,7,78])
print(arr)
aar_w=np.where(arr%2==0,"even","odd")
print(aar_w)

#concatenate
import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([1,2,3])
arr1_arr2=np.concatenate((arr1,arr2))
print(arr1_arr2)
arr3=arr1+arr2
print(arr3)

# example 2d
import numpy as np
arr1 = np.array([[10,20,30],[40,50,60]])
arr2 = np.array([[1,2,3],[4,5,6]])
arr1_arr2 = np.concatenate((arr1,arr2))
print(arr1_arr2)

#statistical function

import numpy as np
a = np.array([[10,20,30],[40,50,60]])

b=np.sum(a)
print(b)
   # Sum of all elements
 
b=np.mean(a)
print(b)
  # Average = Sum of elements / Number of elements
 
b=np.median(a)
print(b)
#Middle value after sorting
 
b=np.min(a)
print(b)
# -> Smallest value in array
 
b=np.max(a)
print(b)
#-> Largest value in array
 
b=np.var(a)
print(b)
#   mean,difference,square,average | (sum = ddof) -> divide by array length
 
np.std(a)
 #  -> Standard Deviation = √Variance
  # -> Measures spread of data
 
np.prod(a)
#   -> Multiplication of all elements
 
np.cumsum(a)
#   -> Cumulative (running) sum
 
np.cumprod(a)
#    -> Cumulative (running) product
 
np.argmin(a)
#    -> Index position of minimum value
 
np.argmax(a)
#    -> Index position of maximum value
 
np.abs(a)
#    -> Converts negative values to positive
 #   -> Absolute value (distance from zero)
np.unique(a)
#    -> Returns unique values only
 #   -> Removes duplicates
 
np.percentile(a, 50)
#    -> Finds percentage-based value
 #   -> 50th percentile = Median
 
np.quantile(a, 0.5)
#    -> Similar to percentile
 #   -> 0.5 = 50%
 
np.ptp(a)
#    -> Range = Max - Min
np.any(a)
#    -> True if at least one value is True
 