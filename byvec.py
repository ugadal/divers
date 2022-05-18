#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
v=[-3,-1,1,3]
ex=[4,-4]
m=[(x,y,z) for x in ex for y in v for z in v]
m.extend([(y,x,z) for x in ex for y in v for z in v])
m.extend([(y,z,x) for x in ex for y in v for z in v])
print(m)
print(len(m))
dr=[(4,y,z) for y in v for z in v]
ga=[(-4,y,z) for y in v for z in v]
top=[(x,y,4) for x in v for y in v]
bot=[(x,y,-4) for x in v for y in v]
rear=[(x,4,z) for x in v for z in v]
front=[(x,-4,z) for x in v for z in v]
af=dr+ga+top+bot+rear+front
FACES={}
print (dr)
x4= [(x,y,z) for x,y,z in af if x>=3]
x3= [(x,y,z) for x,y,z in af if x==1]
x2= [(x,y,z) for x,y,z in af if x==-1]
x1= [(x,y,z) for x,y,z in af if x<=-3]
y4= [(x,y,z) for x,y,z in af if y>=3]
y3= [(x,y,z) for x,y,z in af if y==1]
y2= [(x,y,z) for x,y,z in af if y==-1]
y1= [(x,y,z) for x,y,z in af if y<=-3]
z4= [(x,y,z) for x,y,z in af if z>=3]
z3= [(x,y,z) for x,y,z in af if z==1]
z2= [(x,y,z) for x,y,z in af if z==-1]
z1= [(x,y,z) for x,y,z in af if z<=-3]
# ~ for g in [x1,x2,x3,x4]:print("g",len(g),g)
X=[]
X.append(x1)
X.append(x2)
X.append(x3)
X.append(x4)
Y=[]
Y.append(y1)
Y.append(y2)
Y.append(y3)
Y.append(y4)
Z=[]
Z.append(z1)
Z.append(z2)
Z.append(z3)
Z.append(z4)
for xxx in range(4):print(xxx,len(X[xxx]))
for f in dr:FACES[f]=f
drr=[(x,z,-y) for x,y,z in dr]
print(drr)
np=list(FACES[f] for f in drr)
for to,fro in zip(dr,np):FACES[to]=fro
for f in dr:print(f,FACES[f])
