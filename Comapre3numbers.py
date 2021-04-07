'''1.Create a program to compare three numbers 
and find the bigger numbers. 
[topics covered: identified, variable, types, 
operator, if statement]'''
'''a=int(input("Enter a Number "))
b=int(input("Enter a Number "))
c=int(input("Enter a Number "))
if(a>b) and (a>c):
    print(a,"is bigger")
elif(b>a) and (b>c):
    print(b,"is bigger")
else:
    print(c,"is bigger")'''
'''Using Function'''
def calculate_big(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
'''a=int(input('Enter a number '))
b=int(input('Enter a number '))
c=int(input('Enter a number '))
print(calculate_big(a,b,c),'is a big number')'''