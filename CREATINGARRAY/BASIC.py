# 1D Array Creation Example
"""
import numpy as np

anand=np.array([9,0,5,6,6])
print(anand)
"""

# 2D ARRAY Creation Example 

"""import numpy as np
anand2=np.array([[9,5,6,7,9,0],[9,5,7,8,3,2]])
print(anand2)

"""

# 6D Array Creation Example
"""
import numpy as np
anand3=np.array([[[[[[23,45,2,12],[90,91,92,93],[30,31,32,33]]]]]])
print(anand3)
print("Dimension of Array:", np.ndim(anand3))
print("shape of Array:", anand3.shape)
print("size of array",anand3.size)
print("item size of array",anand3.itemsize)
print("data type of array",anand3.dtype)
print("nbytes of array",anand3.nbytes)
print("number of axis",anand3.ndim)
print("number of elements along axis 0",anand3[0])
print("number of elements along axis 1",anand3.shape[1])
print("number of elements along axis 2",anand3.shape[2])
print("number of elements along axis 3",anand3.shape[3])
print("number of elements along axis 4",anand3.shape[4])
print("number of elements along axis 5",anand3.shape[5])

print("number of elements along axis -1",anand3.shape[-1])
print("number of elements along axis -2",anand3.shape[-2])
print("number of elements along axis -3",anand3.shape[-3])
print("number of elements along axis -4",anand3.shape[-4])
print("number of elements along axis -5",anand3.shape[-5])
print("number of elements along axis -6",anand3.shape[-6])
print("total number of elements",anand3.size)

"""



# ARANGE Function Example

"""
import numpy as np
anand4=np.arange(0 ,11,3)
print(anand4)
print(type(anand4))
print("Dimension of Array:", np.ndim(anand4))
print("shape of Array:", anand4.shape)
print("size of array",anand4.size)
print("item size of array",anand4.itemsize)
print("data type of array",anand4.dtype)
print("nbytes of array",anand4.nbytes)
print("number of axis",anand4.ndim)
"""




# LINSPACE Function Example"
"""
import numpy as np
anand5=np.linspace(0,10,3)
print(anand5)
print(type(anand5))
print("Dimension of array:", np.ndim(anand5))
print("shape of array", anand5.shape)
print("size of array",anand5.size)
print("item size of array",anand5.itemsize)
print("data type of array",anand5.dtype)
print("nbytes of array",anand5.nbytes)
print("number of axis",anand5.ndim)

"""
# ZEROS Function Example

"""
import numpy as np 
anand6=np.zeros((4,3))
print(anand6)
print("shpae of array",anand6.shape)
print("size of array:", anand6.size)
print(type(anand6))
print("Dimesion pf array :", np.ndim(anand6))
print("item size of array",anand6.itemsize)
print("data type of array",anand6.dtype)
print("nbytes of array",anand6.nbytes)
print("number of axis",anand6.ndim)
"""

# FULL Function Example

"""
import numpy as np
anand7=np.full((4,3),5)
print(anand7)
print("Dimension of array:",np.ndim(anand7))
print("size of array:", anand7.size)
print("size of array:", np.size)
print("shape of array",anand7.shape)
print("shape of array",np.shape(anand7))
print(type(anand7))
print("item size of array:", anand7.itemsize)
print("byte in array:", anand7.nbytes)

"""

# ONES Function Example

"""
import numpy as np 
anand8=np.ones((3,4))
print(anand8)
print("Dimension of array:",np.ndim(anand8))
print("size of array:", anand8.size)
print("size of array:", np.size(anand8))
print("shape of array",anand8.shape)
print("shape of array",np.shape(anand8))
print(type(anand8))
print("item size of array:", anand8.itemsize)
print("byte in array:", anand8.nbytes)
"""

# IDENTITY Function Example
"""
import numpy as np
anand9=np.eye(3,4)
print(anand9)
print("Dimension of array:",np.ndim(anand9))
print("size of array:", anand9.size)
print("size of array:", np.size(anand9))
print("shape of array",anand9.shape)
print("shape of array",np.shape(anand9))
print(type(anand9))
print("item size of array:", anand9.itemsize)
print("byte in array:", anand9.nbytes)
"""

# RANDOM Function For float  Example
"""

import numpy as np
anand10=np.random.rand(3,4)
print(anand10)
print("Dimension of array:",np.ndim(anand10))
print("size of array:", anand10.size)
print("size of array:", np.size(anand10))
print("shape of array",anand10.shape)
print("shape of array",np.shape(anand10))
print(type(anand10))
print("item size of array:", anand10.itemsize)
print("byte in array:", anand10.nbytes)

"""


# RANDOM Function For Integer Example

"""
import numpy as np
anand11=np.random.randint(1,10,(3,4))
print(anand11)
print("Dimension of array:",np.ndim(anand11))
print("size of array:", anand11.size)
print("size of array:", np.size(anand11))
print("shape of array",anand11.shape)
print("shape of array",np.shape(anand11))
print(type(anand11))
print("item size of array:", anand11.itemsize)
print("byte in array:", anand11.nbytes)

"""
# astype Function Example


"""
import numpy as np
anand12=np.array([1,2,3,4,5])
anand12=anand12.astype('int64')
print(anand12)
print("Dimension of array:",np.ndim(anand12))
print("size of array:", anand12.size)
print("size of array:", np.size(anand12))
print("shape of array",anand12.shape)
print("shape of array",np.shape(anand12))
print(type(anand12))
print("item size of array:", anand12.itemsize)
print("byte in array:", anand12.nbytes)
print("data type of array",anand12.dtype)
"""