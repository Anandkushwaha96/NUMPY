#dot function

""""
import numpy as np 
arr=np.array([[1,2,3,4],[5,6,7,8]])
arr1=np.array([[12,32,8,9],[7,8,11,23]])
print(np.dot(arr,arr1.transpose()))  #dot product of two arrays
"""
"""
#dot product of two matrices

import numpy as np 
arr=np.array([[2,-2],[5,3]])
arr1=np.array([[-1,4],[7,-6]])
print(np.dot(arr,arr1))
"""

#inverse of a matrix

import numpy as np
arr=np.array([[1,2],[3,4]])
print(np.linalg.inv(arr))