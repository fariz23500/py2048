



import getch
n=int(input("enter board size \n"))
w=int(input("enter number required for winning\n"))
count1=0
count2=0
count3=0
count4=0
import random

board=[]
i=1
j=1

for i in range(n):
    s=[]
    for j in range(n):
        s.append(0)
    board.append(s)

def print1(game1):
    d=0
    for k in range(n):
        print(game1[d])
        print("\n")
        d=d+1
    return 0

def right(game):
   
    l=0
    m=0
    count1=0
    z=n
    t=n-1
    for i in range(n):
        for l in range(z):
            for m in range(t):
                z=m+1
        
                k=n-1-m
                for p in range(k):
                    if game[l][m]==game[l][z]:
                    
                        game[l][z]*=2
                        if game[l][z] !=0:
                            count1+=1
            
                        game[l][m]=0
                    elif game[l][z] != 0:
                        break
                    elif game[l][z]==0:
                        game[l][z],game[l][m]=game[l][m],game[l][z]
                        if game[l][z] !=0:
                            count1+=1
                    z=z+1
            
        
    
    return game,count1

def left(game):
    count2=0
    for i in range(n):
        for l in range(n):
            for m in reversed(range(n)):
                k=m
                for z in reversed(range(k)):
                    if game[l][m]==game[l][z]:
                        game[l][z]*=2
                        if game[l][z] !=0:
                            count2+=1
                        game[l][m]=0
                    elif game[l][z]!=0:
                        break
                    elif game[l][z]==0:
                        game[l][z],game[l][m]=game[l][m],game[l][z]
                        if game[l][z] !=0:
                            count2+=1
    
        
    
    return game,count2

def down(game):
   
    l=0
    m=0
    count3=0
    z=n-1
    t=n
    for i in range(n):
        for l in range(z):
            for m in range(t):
                z=l+1
        
                k=n-1-l
                for p in range(k):
                    if game[l][m]==game[z][m]:
                    
                        game[z][m]*=2
                        if game[z][m] !=0:
                            count3+=1
            
                        game[l][m]=0
                    elif game[z][m] != 0:
                        break
                    elif game[z][m]==0:
                        game[z][m],game[l][m]=game[l][m],game[z][m]
                        if game[z][m] !=0:
                            count3+=1
                    z=z+1
            
        
    print(count3)
    return game,count3
    

def up(game):
    
    l=0
    m=0
    count4=0
    z=n
    t=n
    for i in range(n):
        for l in reversed(range(z)):
            for m in range(t):
                z=l-1
        
                k=l
                for p in range(k):
                    if game[l][m]==game[z][m]:
                    
                        game[z][m]*=2
                        if game[l][m] !=0:
                            count4+=1
            
                        game[l][m]=0
                    elif game[z][m] != 0:
                        break
                    elif game[z][m]==0:
                        game[z][m],game[l][m]=game[l][m],game[z][m]
                        if game[z][m] !=0:
                            count4+=1
                        
                        
                    z=z-1
            
        
    
    return game,count4
def rand(game):
    flag=False
    while flag!=True :
        p=n-1
        c=random.randint(0,p)
        r=random.randint(0,p)
        if game[r][c]==0:
            game[r][c]=2
            flag=True
    print1(game)
    return game
def winner(game):   

    for i in range(n):
        for j in range(n):
            if game[i][j]==w:
                return 1
def check(game):
    flag=0
    for i in range(n):
        for j in range(n):
            if game[i][j]==0:
                flag=1
    for i in range(n):
        for j in range(n-1):
            if game[i][j]==game[i][j+1]:
                flag=1
    if flag==0:
        return 1
k1=0
game1=board
game1=rand(game1)

while k1!=1:
    i1=getch.getch()
    if i1=="d":
        game1,count1=right(game1)
        if count1!=0:
            game1=rand(game1)
            count1=0
        else:
            print("enter a valid input")
            print1(game1)
    elif i1=="a":
        game1,count2=left(game1)
        if count2!=0:
            game1=rand(game1)
            count2=0
        else:
            print("enter a valid input")
            print1(game1)
    elif i1=="w":
        game1,count4=up(game1)
        if count4!=0:
            game1=rand(game1)
            count4=0
        else:
            print("enter a valid input")
            print1(game1)
    elif i1=="s":
        game1,count3=down(game1)
        if count3!=0:
            game1=rand(game1)
            count3=0
        else:
            print("enter a valid input")
            print1(game1)
    k1=winner(game1)
    k2=check(game1)
    if k2==1:
        print("you have lost")
        break
    if k1==1:
        print("you have won")
        break
        

