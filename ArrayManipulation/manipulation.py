#Reshape function
"""
import numpy as np 
arr=np.array([[1,2,3,4,5,6,7,8]])
print(arr.shape)
newarr=arr.reshape([2,4])
print(newarr)
print(newarr.shape)
"""
#reshape with unknown dimension

"""
import numpy as np

arr=np.arange(1,25).reshape(2,3,4)
print(arr)

print("sum of axis 0:\n",np.sum(arr,axis=0))
print("sum of axis 1:\n",np.sum(arr,axis=1))
print("sum of axis 2:\n",np.sum(arr,axis=2))
print(arr[0])
print(arr[1])
print(arr[2])
"""


#sum function with axis parameter
"""


import numpy as np

arr=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr)
print(arr.shape)
print("sum of axis 0\n ",arr.sum(axis=0))
print("sum of axis 1\n ",arr.sum(axis=1))
print("sum of axis 2\n ",arr.sum(axis=2))
"""

#transpose function 
"""
import numpy as np

arr=np.array([[1,2,3,4,5,6,7,8,9,10]]).reshape(2,5)
print(arr.T)

"""

#flatten function
"""
import numpy as np 

arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.flatten())
print(arr.flatten(order='F'))
print(arr.flatten(order='A'))
print(arr.flatten(order='C'))
print(arr.flatten(order='K'))
"""



#concatenate function
"""
import numpy as np
arr=np.array([[1,2,3]])
arr1=np.array([[7,8,9]])
print(np.concatenate((arr,arr1),axis=0))

"""

#Vstack function
"""
import numpy as np
arr=np.array([[1,2,3]])
arr1=np.array([[7,8,9]])
print(np.vstack((arr,arr1)))
"""

#Hstack function
"""
import numpy as np

arr=np.array([[1,2,3]])
arr1=np.array([[7,8,9]])
print(np.hstack((arr,arr1)))
"""

#split function

import numpy as np
arr=np.array([[1,2,3,4,5,6,7,8]])
newarr=np.split(arr,3)
print(newarr)

