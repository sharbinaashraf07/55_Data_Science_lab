import numpy as np

ar = np.array([[2,4,3,],[3,6,8]])
d = np.diag(ar)
print(d)
print("sum =",sum(d))