days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
months={'Jan','Feb','March'}
print(days)
print(months)
print(type(days))
print(type(months))
for d in days:
    print(d)
days.add("Sun")
print(days)
days.discard("Sun")
print(days)
print("Mon" in days)
print("Sun" in days)
a=set('aabdbdcb2rcowenc3rr')
print(a)
b=set('bucjaald932neasknf')
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
a={x for x in 'ancdefgh' if x not in 'anc'}
print(a)
#l=[1,23,4,56,5]
for i,v in enumerate(a):
    print(v,' in ',i,' index')

