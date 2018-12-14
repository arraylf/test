from Tkinter import *
from random import *
from time import *

def main():
    def displaytime():
        t2=int(time())
        v.set(t2-t)
              
    def restart():
        global t
        t=int(time())
        a=numbergrid()
        a.create_answer()
        a.create_issue2()
        for i in xrange(81):
            if a.issue2[i]!=0:
                Label(text=a.issue2[i],
                      width=3,justify='c').grid(row=i%9,column=i/9)
            else:
                Entry(fg='blue',width=3,justify='c').grid(row=i%9,column=i/9)
        
    root=Tk()
    root.title('shudu')
    restart()
    v=StringVar()
    v.set(0)
    Button(text='restart',command=restart).grid(row=9,columnspan=2)
    Button(textvariable=v,command=displaytime
           ).grid(row=9,column=3,columnspan=2)
    root.mainloop()

class numbergrid():
    def __init__(self):
        self.answer=[0]*81
        self.issue=self.answer[:]
        self.issue1=self.answer[:]
        self.issue2=self.answer[:]
        self.location=self.answer[:]
        self.maybelocation=self.answer[:]
        self.maybevalue=self.answer[:]
        self.i=0
        self.n=0
    
    def create_answer(self):
        i=0
        while i<81:
            l=self.return_list(i)
            l1=l[:]
            v=i/9+1
            for j in l1:
                if self.chick(j,v):
                    l.remove(j)
            self.maybelocation[i]=l[:]
            if len(l)!=0:
                a=choice(l)
                self.answer[a]=v
                self.location[i]=a
                i+=1
            else:
                self.recall(i-1)
                i=self.i

    def create_issue(self,n=42):
        m=range(81)
        shuffle(m)
        self.issue=self.answer[:]
        for i in range(n):
            self.issue[m[i]]=0
        self.n=n

    def create_issue1(self):
        self.issue1=self.answer[:]
        m=range(81)
        shuffle(m)
        for i in m:
            self.maybevalue[i]=range(1,10)
            self.normalchick(i,self.issue1)
            if len(self.maybevalue[i])==1:
                self.issue1[i]=0
        self.n=self.issue1.count(0)

    def create_issue2(self):
        self.issue2=self.answer[:]
        m=range(81)
        shuffle(m)
        for i in m:
            self.maybevalue[i]=range(1,10)
            self.normalchick(i,self.issue2)
            if len(self.maybevalue[i])==1:
                self.issue2[i]=0
            else:
                self.highchick(i,self.issue2)
        self.n=self.issue2.count(0)

    def resolve_issue(self,issue):
        pass

    def normalchick(self,index,issue):
        l=self.return_list1(index)
        for i in range(len(l)):
            l[i]=issue[l[i]]
        for i in range(1,10):
            if i in l:
                self.maybevalue[index].remove(i)

    def highchick(self,index,issue):
        l=[[],[],[]]
        value=issue[index]
        issue[index]=0
        m=self.return_list1(index)
        n=0
        for i in m:
            if issue[i]==0:
                self.maybevalue[i]=range(1,10)
                self.normalchick(i,issue)
                if i/9==index/9:
                    l[0]+=self.maybevalue[i]
                if i%9==index%9:
                    l[1]+=self.maybevalue[i]
                if i/27*3+i%9/3==index/27*3+index%9/3:
                    l[2]+=self.maybevalue[i]
        if value not in l[0]:
            value=0
        elif value not in l[1]:
            value=0
        elif value not in l[2]:
            value=0                    
        issue[index]=value
            
    def chick(self,index,value):
        l=[]
        for i in range(9):
            l+=[index/9*9+i,i*9+index%9]
        l.remove(index)
        l.remove(index)
        l.sort()
        if self.answer[index]!=0:
            return True
        for i in l:
            if value==self.answer[i]:
                return True
                                    
    def return_list(self,index):
        l=[0,1,2,9,10,11,18,19,20]
        l1=[0]*9
        j=index%9
        for i in range(9):
            l1[i]=l[i]+j/3*27+j%3*3
        return l1

    def return_list1(self,index):
        l=[i for i in range(81) if(i%9==index%9 or i/9==index/9
                        or i/27*3+i%9/3==index/27*3+index%9/3)]
        l.remove(index)
        return l
    
    def recall(self,i):
        self.maybelocation[i].remove(self.location[i])
        self.answer[self.location[i]]=0
        self.location[i]=0
        if len(self.maybelocation[i])==0:            
            self.recall(i-1)
        else:
            self.location[i]=choice(self.maybelocation[i])
            self.answer[self.location[i]]=i/9+1
            self.i=i+1
            
    def print_list(self,l):
        for i in xrange(len(l)):
            if i%9==8 :
                print l[i]
            else:
                print l[i],

main()
