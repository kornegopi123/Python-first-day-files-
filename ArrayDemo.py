from array import *
ar1=array("i",[1,2,3,4,5])
print(ar1)
ar1.insert(0,22)
print(ar1)
ar1.append(30)
print(ar1)
print(ar1.count(1))
ar1.extend([100,200])
print(ar1)
ar1.fromlist([1000,2000])
print(ar1)
print(ar1.index(22))
print(ar1.pop())
ar1.remove(1)
print(ar1)
print(type(ar1))
ar1.reverse()
print(ar1)
print()
print(ar1.tobytes())
print()
print(ar1.tolist())
print(type(ar1))