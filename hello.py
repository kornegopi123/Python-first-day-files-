'''1.Create a program to compare three numbers 
and find the bigger numbers. 
[topics covered: identified, variable, types, 
operator, if statement]

a=int(input("Enter a Number "))
b=int(input("Enter a Number "))
c=int(input("Enter a Number "))
if(a>b) and (a>c):
    print(a,"is bigger")
elif(b>a) and (b>c):
    print(b,"is bigger")
else:
    print(c,"is bigger")
    '''
'''2.
def calculate_big(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input('Enter a number '))
b=int(input('Enter a number '))
c=int(input('Enter a number '))
print(calculate_big(a,b,c),'is a big number')'''

'''3.Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them 
the year that they will turn 100 years old

name=input('Enter your name :')
age=int(input('Enter your age:'))
print(name,"you will get 100 years on",(100-age)+2021)'''

def age_calc(name,age):
    return ((100-age)+2021)
name=input('Enter your name: ')
age=int(input('Enter your age: '))
print(name,'you will get 100 years on',age_calc(name,age))

''' For Loop and Range Demo
for i in range(0,10):
    print(i)
for i in range(0,10,2):
    print(i)
for i in range(-100,-10,10):
    print(i)    
    '''
    
'''#6.Rock beats scissors, Scissors beats paper, Paper beats rock
player1=input("enter player 1 name ")
player2=input("enter player 2 name ")
res=0
while True:
    print("player1 enter your choice \n1.rock \n2.paper\n3.scissor\n")
    choice=int(input())
    print("player2 enter your choice ")
    choice2=int(input())
    if((choice==1 and choice2==2) or(choice==2 and choice2==1)):
        res=2
    elif((choice==1 and choice2==3) or (choice==3 and choice2==1)):
        res=1
    else :
        res=3
        
    if(choice==choice2):
        print("DRAW");
    elif res==choice:
        print(player1,"wins ")
    else:
        print(player2,"wins")
        
    print("do you want to play again? y/n")
    d=input()
    if d=='n' or d=='N':
        break
''' 
'''4.Take two lists, say for example these two:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common 
between the lists (without duplicates). Make sure your program works on two lists of different 
sizes.
a=[]
b=[]
c=[]
al=int(input('Enter first list length '))
bl=int(input('Enter second list length '))
for a1 in range(1,al+1):
    print('element ',a1)
    a.append(int(input()))
for b1 in range(1,bl+1):
    print('element ',b1)
    b.append(int(input()))
for i in a:
    for j in b:
        if (j in a) and (j not in c):
            c.append(j)
print(c)
'''
'''def adding(n1,n2):
    return n1+n2
print(adding(10,20))
print(adding())'''
        

