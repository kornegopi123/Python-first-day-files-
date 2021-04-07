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
