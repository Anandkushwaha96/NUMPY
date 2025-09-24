
"""
import numpy as np

#seed function 

np.random.seed(10)
print(np.random.rand(3))  #2 rows and 3 columns random values between 0 and 1


"""

"""

import numpy as np

#  Without seed, numbers change on every run.

print(np.random.rand(3))  #2 rows and 3 columns random values between 0 and 1
"""
"""
import numpy as np 
np.random.seed(10)
print(np.random.randn(3))

"""

#randint function
"""
import numpy as np
S=np.random.randint(1,10,10)
print(S)  #random integer between 1 and 10

"""

#ranmom choice function
"""
import numpy as np

arr=np.array([2,3,4,5,6,76,778,8])
P=np.random.choice(arr,3)  #randomly choose 3 values from the array
print(P)

"""

#shuffle function
import numpy as np
arr=np.array([2,3,4,5,6,76,778,8])
T=np.random.shuffle(arr)
print(arr)  #shuffle the array randomly