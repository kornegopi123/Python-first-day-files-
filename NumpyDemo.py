from numpy  import *
import matplotlib

a1=array([1,2,3,4])
print(type(a1))
fam=["liz", 1.73, "emma", 1.68,"mom", 1.71, "dad", 1.89]
print(type(fam))
fam_ext=fam+['me',1.79]
print(fam_ext)

height=[1.73,1.68,1.71,1.89,1.79]
weight=[65.4,59.2,63.6,88.4,68.7]
#print(weight/height**2)
np_height=array(height)
np_weight=array(weight)
bmi=np_weight/np_height**2
print(bmi)
np_arr=array([98,10])
print(np_arr+np_arr)

a = np.zeros((2,2))   # Create an array of all zeros
print(a) 
b = np.ones((1,2))    # Create an array of all ones
print(b)
c = np.full((2,2), 7)  # Create a constant array
print(c)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(b)
print(a[0, 1])
b[0, 0] = 77
print(a[0, 1])
row_r1 = a[1, :] 
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape) 
print(row_r2, row_r2.shape)

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))
print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))
print(x / y)
print(np.divide(x, y))
print(np.sqrt(x))