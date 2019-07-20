def dist(a,b):
    if(len(a)!=len(b)):
        return 0
    else:
        s=0
        for i in range(len(a)):
            s+=(a[i]-b[i])**2

        print(s)
        return s**0.5
def mean(c,l):
    p=l[c[0]]
    print(p)
    for i in range(1,len(c)):
        for j in range(len(l[c[i]])):
            print(l[c[i]][j])
            p[j]=p[j]+l[c[i]][j]
    for i in range(len(c)):
        p[i]/=len(c)

    return p

def cluster(l):
    print(l)
    c1=[]
    c2=[]
    for i in range(len(l)):
        if(i%2==0):
            c1.append(i)
        else:
            c2.append(i)
    c3=[]
    c4=[]
    c=[]
    p=[]
    while((c1!=c3)and(c2!=c4)):
        m1=mean(c1,l)
        m2=mean(c2,l)
        for i in l:
            p.append(dist(i,m1))
            p.append(dist(i,m2))
            c.append(p)
            p=[]
        for i in c:
            print("   m1   m2")
            for j in i:
                print(j,"  ",end="")
            print("\n")
        print(c)
        for i in range(len(c[1])):
            if(c[0][i]<c[1][i]):
                c3.append(i)
            else:
                c4.append(i)
        t=c1
        c1=c3
        c3=t
        t=c2
        c2=c4
        c4=c2

    return(c1,c2)
