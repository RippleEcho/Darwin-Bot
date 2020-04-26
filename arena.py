from match import match
from repbot import repbot
import random
import math
class arena:
    def __init__(self):
        self.A=0

    def setup(self,N,M,R,G):
        B=[]
        C=[]
        for n in range(N):
            B.append(self.genbot())
            C.append(M)
        for g in range(G):
            C.clear()
            for n in range(N):
               C.append(M) 
            K=self.tourn(B,C,R)
            if(g<G-1):
                B=self.evolve(B,K)
        W=C.index(max(C))
        print(B[W].sout(B[W].mind))

    def genbot(self):
        BMS=""
        random.seed()
        for h in range(216):
            BMS=BMS+str(random.randint(0,5))
        return repbot(BMS)

    def tourn(self,B,C,R):
        for N in range(R):
            A=self.Round(B,C)
            C=self.Judge(B,A,sum(C))
        W=C.index(max(C))
        H,Q=0,0
        A=sorted(C)
        A.reverse()
        for q in range(int(len(B)/4)):
            Q+=A[q]
        for h in range(int(len(B)/2)):
            H+=A[h]
        print("Top sing: " +str(max(C))+" / "+str(sum(C)))
        print("Top quar: " +str(Q)+" / "+str(sum(C)))
        print("Top half: " +str(H)+" / "+str(sum(C)))
        #print(B[W].sout(B[W].mind))
        print(B[W].reduce())
        return C

    def evolve(self,B,C):
        #in:bots, bot counts
        #out:new bots
        R=int(len(B)/4)
        for h in range(2*R):
            L=C.index(min(C))
            B.pop(L)
            C.pop(L)
        W=C.index(max(C))
        for g in range(R):
            B.append(repbot(B[W].sout(B[W].muta(B[W].mind))))
        for f in range(R):
            B.append(self.genbot())
        return B
            

    def Round(self,B,C):
        #in:bots, bot counts
        #out:points for bots
        E=[]
        P=[]
        for N in range(len(B)):
            P.append(0)
            #print(C)
            for M in range(C[N]):
                E.append((B[N],N))
        F=random.sample(E,len(E))
        S=[]
        for t in range(0,len(F),2):
            u=random.randint(90,110)
            o=match(F[t][0],F[t+1][0],u)
            r=o.run()
            S.append(r[0])
            S.append(r[1])
        for T in range(len(F)):
            P[F[T][1]]+=S[T]
        return P

    def Judge(self,B,P,T):
        #in: bots, points, pool size
        #out: new copy nums
        S=sum(P)
        c=[]
        if(S==0):
            for g in range(len(B)):
                c.append(int(T/len(B)))
            return c
        
        for g in range(len(B)):
            c.append(int(math.floor(P[g]/S)*T))
        while(sum(c)<T):
            d=random.randint(0,len(B))
            v=1.00
            for h in range(len(B)):
                if(P[h]==0):
                    k=1.00
                else:
                    k=float(c[h]/P[h])*float(T/(len(B)))
                if(k<v and P[h]!=0):
                    d=h
                    v=k
            c[d]+=1
        return c
a=arena()
a.setup(32,32,128,256)
