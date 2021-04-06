'''3.Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them 
the year that they will turn 100 years old'''

name=input('Enter your name :')
age=int(input('Enter your age:'))
print(name,"you will get 100 years on",(100-age)+2021)


'''Using Function'''
def age_calc(name,age):
    return ((100-age)+2021)
name=input('Enter your name: ')
age=int(input('Enter your age: '))
print(name,'you will get 100 years on',age_calc(name,age))

