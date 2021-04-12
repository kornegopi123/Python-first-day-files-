
d={}
print(type(d))
d={'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(d)
d['year']=1999
print(d)
print(d['Name'])
d1={'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(d1)
d1.clear()
print(d1)
del d1
print(len(d))
print(str(d))
print(d.items())
print(d.get('Name'))
#print(d.has_key('k'))
print(d.keys())
print(d.values())
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
d.setdefault('Name')
print(d)
d1={'key':'value'}
d.update(d1)
print(d)