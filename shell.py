import random
import math

def bot(mine,your):
    #6 x 6 x 6 mind array
    M=[]
    x=sum(mine)%6
    y=sum(your)%6
    if(len(mine)==0):
        s=0
        for a in M:
            for b in a:
                for c in b:
                    s+=c
        return s%6

    for z in range(6):
        p=M[z][y][x]
        if(p==5):
            p=random.randint(1,4)
        if(p==4):
            (x,y)=(x,(y-1)%6)
        if(p==3):
            (x,y)=((x-1)%6,y)
        if(p==2):
            (x,y)=(x,(y+1)%6)
        if(p==1):
            (x,y)=((x+1)%6,y)
        if(p==0):
            (x,y)=(x,y)
    if(len(mine)%2==0):
        return x
    else:
        return y
