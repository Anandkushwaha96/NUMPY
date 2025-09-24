#sort functions
"""
import numpy as np
arr=np.array([[3,2,0],[1,4,5]])
print(np.sort(arr , axis=0))

"""
#arg sort function 
"""
import numpy as np
arr=np.array([[3,2,0],[1,4,5]])
print("index based sort all:\n",np.argsort(arr))
print("index based sort axis 0:\n",np.argsort(arr, axis=0))
print("index based sort axis 1:\n",np.argsort(arr, axis=1))

"""

# Where function
"""
import numpy as np 

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np.where(arr>5))
print(np.argwhere(arr>5))
"""

#Unique function
"""
import numpy as np

arr=np.array([[1,2,3,4],[5,5,6,7],[8,9,9,10],[1,23,45,66]])
print(np.unique(arr))
"""

#in1d function

import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9])
arr1=np.array([[2,45,56,78],[12,23,24,25]])
print(np.in1d(arr,arr1))