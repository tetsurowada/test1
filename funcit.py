import numpy as np
import matplotlib.pyplot as plt
F=[-3,5,9,11]
G=[-3,3,5,7]
M=3
n=M+1
m=M+1
f=np.zeros((4,4))
for s in range (n):
    for x in range(m):
        if x>s:
            f[s][x]=-100
        else:
            f[s][x]=F[x]+G[s-x]
p=[]
for x in range(m):
    Pk=np.zeros((n,n))
    for i in range(n):
        j= i-x+1
        j=max([1,j])
        j=min([n,j])
        Pk[i][j-1]=Pk[i][j-1]+0.4
        j+=1
        j=max([1,j])
        j=min([n,j])
        Pk[i][j-1]=Pk[i][j-1]+0.6
    p.append(Pk)
v=np.array([-16,-8,4,2])
def funcit(f,p,delta,v,tol):
    count=1
    y=[]
    while count<100:
        pv=[i@v for i in p]
        pva=np.array(pv)
        new=f+delta*pva
        v_new=np.max(new,axis=1)
        xpol=np.argmax(new,axis=1)
        print(v_new,xpol)
        y.append(v_new[0])
        if np.linalg.norm(v_new-v)<tol:
            x=np.linspace(1,count,count)
            plt.subplot(2,2,1)
            plt.plot(x,y)
            S=np.linspace(0,len(f)-1,len(f))
            plt.subplot(2,2,2)
            plt.bar(S,xpol)
            plt.xlabel("Stock")
            plt.ylabel("Optimal Irrigation")
            plt.subplot(2,2,3)
            plt.bar(S,v_new)
            plt.xlabel("Stock")
            plt.ylabel("Optimal Value")
            return v_new,xpol,
        v=v_new
        count+=1
    
    


funcit(f,p,0.9,v,0.01)


