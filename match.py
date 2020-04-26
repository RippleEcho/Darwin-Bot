from repbot import repbot
import random
class match:
    def __init__(self, botA, botB, turns):
        self.a=botA
        self.b=botB
        self.N=turns
        
    def run(self):
        AT=0
        BT=0
        AM=[]
        BM=[]
        while (self.N>0):
            self.N-=1
            AX=self.a.work(AM,BM)
            BX=self.b.work(BM,AM)
            #print(AX,BX)
            if(AX+BX<6):
                AT+=AX
                BT+=BX
            AM.append(AX)
            BM.append(BX)
        return(AT,BT)
