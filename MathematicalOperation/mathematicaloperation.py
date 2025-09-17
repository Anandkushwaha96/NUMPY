# add function 
"""
import numpy as np
arr= np.array([23,12,34,545])

print(np.add(arr,24))
"""

#subtract function
"""
import numpy as np
arr=np.array([23,25,39,20])
print(np.subtract(arr,12))

"""
#multiply function
"""
import numpy as np
arr=np.array([24,35,6,70])

print(np.multiply(arr,3))

"""
#Divide function
"""
import numpy as np

arr=np.array([[3,24,5,67],
              [90,45,34,56],
              [20,38,45,69]])
print(np.divide(arr,2))
print(type(arr))

"""

#sqrt function
"""
import numpy as np
arr=np.array([[3,24,5,67],
              [90,45,34,56],
              [20,38,45,69]])
print(np.sqrt(arr))
print(type(arr))

"""

#exp function
"""
import numpy as np
arr=np.array([[3,24,5,67],
              [90,45,34,56],
              [20,38,45,69]])
print(np.exp(arr))
"""

# power function
"""
import numpy as np
arr=np.array([[23,45,67,89],
              [12,34,56,78],
              [90,21,43,65]])
print(np.power(arr,3))

"""

#mod(remainder or modular operation) function

"""

import numpy as np
arr=np.array([[23,45,67,89],
              [12,34,56,78]])
print(np.mod(arr,2))
"""

#sum function 

"""
import numpy as np 
arr=np.array([[23,45,67,89],
              [12,34,56,78]])

print(np.sum(arr))


"""
 #cumsum function
"""
import numpy as np 

arr= np.array([[23,45,67,89],
               [23,45,89,90]])
print(np.cumsum(arr))


"""

#cumprod function
"""
import numpy as np 
arr=np.array([1,2,3,4])

print(np.cumprod(arr))
"""

#prod function 
"""
import numpy as np 
arr=np.array([1,2,3,4])
print(np.prod(arr))

"""

#sum function with axis parameter
import numpy as np

arr=np.array([[4,5,6],[9,2,3],[8,4,7]])

print(np.sum(arr,axis=0))
print(np.sum(arr, axis=1))
print(np.sum(arr, axis=-1))
print(np.sum(arr, axis=0))