t=()
t=(2,3,5,'gopi','korne')
print(t)
print(t[0])
print(t[0:4])
print(t[::])
print(t[:3])
print(t[2:])
u=t,(1,2,34,4)
print(u)
#t[0]=988 it throws error because tuple elements are immutable
single='hello',
print(single)
tup3=t+single
print(tup3)
print(len(tup3))
print(('hi',)*4)
for x in tup3:
    print(x)
print(3 in tup3)
tup4=(1,2,3,4,7,8)
print(min(tup4))
print(max(tup4))
print(tuple([1,2,'k','l']))