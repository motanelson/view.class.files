print("\033c\033[47;31m/give me the class file to view ? ")
a=input().strip()
#a="Hello.class"
f1=open(a,"rb")
b=f1.read()
f1.close()
j=False
t=False
l=[]
for c in b:
    if len(l)==2:
        l.append(c)
        i:int=int(c)
        print("\n"+str(i)+" " ,end =" ")
        
        t=True
    if c==1:
        l.clear()
        l.append(1)
    if c==0 and len(l)==1:
        if l[0]==1:
            l.append(0)
        
    if t and c>31 and c<129:
        cc=chr(c)
    
        print(cc,end="")
        j=True
    