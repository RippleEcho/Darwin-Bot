import random
class repbot:
    def __init__(self,SM):
        self.mind=self.cube(SM)

    def cube(self,S):
        T=[]
        for i in range(6):
            T.append([])
            for j in range(6):
                T[i].append([])
                for k in range(6):
                    T[i][j].append(int(S[k+6*j+36*i]))
        return T

    def sout(self,M):
        S=""
        for R in range(216):
            X,Y,Z=R%6,int(R/6)%6,int(R/36)%6
            S=S+str(M[Z][Y][X])
        return S

    def muta(self):
        M=self.mind
        for g in range(6):
            R=random.randint(0,215)
            X,Y,Z=R%6,int(R/6)%6,int(R/36)%6
            M[Z][Y][X]=random.randint(0,5)
        return M
                    
    def foil(self,x,y,z):
        p=self.mind[z][y][x]
        if(p==5):
            p=random.randint(1,4)
        if(p==4):
            return (x,(y-1)%6)
        if(p==3):
            return ((x-1)%6,y)
        if(p==2):
            return (x,(y+1)%6)
        if(p==1):
            return ((x+1)%6,y)
        if(p==0):
            return (x,y)
        return (x,y)

    def work(self,x,y):
        if(len(x)==0):
            s=0
            for a in self.mind:
                for b in a:
                    for c in b:
                        s+=c
            return s%6
        xf=sum(x)%6
        yf=sum(y)%6
        for z in range(6):
            (xf,yf)=self.foil(xf,yf,z)
        if(len(x)%2==0):
            return xf
        else:
            return yf


