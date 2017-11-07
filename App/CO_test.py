#!/usr/bin/python
# -*- coding: UTF-8 -*-

logic  = [3,1,0,0]
toggle = [1,1,0,0]
setval = [1,0,0,1]
thrhld = [0,1,2,0]
a = [0,0,0,0]
b = [0,0,0,0]
c = [0,0,0,0]
d = [0,0,0,0]
e = [0,0,0,0]

maxv = 10
mco = 18;
v = 0;
f = 1;

def mul(n,m):
    c = [i*m for i in n]
    return c

print "          logic  Toggle   setval   thrhld   Total"
for i in range(1,maxv):
    a = mul(logic,i)
    for j in range(1,maxv):
        b = mul(toggle,j)
        for k in range(1,maxv):
            c = mul(setval,k)
            for l in range(1,maxv):
                d = mul(thrhld,l)
                for n in range(0,len(logic)):
                    e[n] = max(a[n],b[n],c[n],d[n])
                v = sum(m for m in e)
                if v == mco and i > 1 and j > 1 and k >1 and l>1:
                    if f < 10:
                        print "方案",f,"     ",i,"     ",j,"     ",k,"     ",l,"     ",v
                    else:
                        print "方案",f,"    ",i,"     ",j,"     ",k,"     ",l,"     ",v
                    f+=1;
