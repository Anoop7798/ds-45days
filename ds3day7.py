#oops concept
#numpy has single datatype but list has multiple datatype
#tuple -> list -> numpy
#numpy consider method but list cannot

import numpy
#print("hello")
#numpy.arange(12) eg:-1
n=numpy.arange(11)
print(n)
print(type(n))
print(n[0])

#eg:-2
import numpy
n = numpy.arange(12)
d = n.reshape(3,4)
print(type(d))
print(d)

#eg:-3
import numpy
n = numpy.arange(12).reshape(3,4)
print(n)

#eg:-4
import numpy
n= numpy.arange(24).reshape(2,3,4)
print(n)

#eg-5
import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[:,-1])
#or 
import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[0:4:,2])
#or
import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[0:4,-1:3])
#or
import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[0:4,2:4])


#eg:-6

import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[1:3,1])
#or

import numpy
n= numpy.arange(12).reshape(4,3)
print(n)
print(n[1:3,1:2])

