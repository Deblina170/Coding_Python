import numpy as np
lst=[20,25,35,30]
x=26
arr=np.array(lst)
nearest = arr[np.abs(arr-x).argmin()]
print(nearest)
