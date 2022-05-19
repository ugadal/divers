#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from random import choice as ch
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
X=[x1,x2,x3,x4]
Y=[y1,y2,y3,y4]
Z=[z1,z2,z3,z4]
# ~ for xxx in range(4):print(xxx,len(X[xxx]))
# ~ print(len(X+Y+Z))
# ~ AF=[f for f in x for x in y for x in [X,Y,Z]]
# ~ print(AF)
# ~ print(len(AF))
for f in m:FACES[f]=f
# ~ nx4=[(x,z,-y) for x,y,z in x4]
# ~ for x,y in zip(x4,nx4):print(x,y)
# ~ np=list(FACES[f] for f in drr)
# ~ for to,fro in zip(dr,np):FACES[to]=fro
# ~ for f in dr:print(f,FACES[f])
NX=list([list([(x,z,-y) for x,y,z in L]) for L in X])
NY=[[(z,y,-x) for x,y,z in L] for L in Y]
NZ=[[(y,-x,z) for x,y,z in L] for L in Z]
print(NX)
MX=list(zip(X,NX))
MY=list(zip(Y,NY))
MZ=list(zip(Z,NZ))
for p,t in zip(X[0],NX[0]):print(p,t)
# ~ for p in NX[0]:print(p)
# ~ for p in MX[0]:print(p)
# ~ exit()
def mkmov(z):
	f,t=z
	# ~ print(f)
	# ~ print(t)
	v=list([FACES[w] for w in f])
	for ky,val in zip(t,v):FACES[ky]=val
ori=list([FACES[k] for k in m])
# ~ x3=MX[2]
# ~ testable=[("x1",MX[1]),("x2",MX[2]),("y1",MY[1])]
# ~ testable=[("x1",MX[1]),("y1",MY[1])]
# ~ testable=[("x1",MX[1]),("x2",MX[2]),("z1",MZ[1])]
testable=[("x0",MX[0]),("x1",MX[1]),("x2",MX[2]),("x3",MX[3])]
testable.extend([("y0",MY[0]),("y1",MY[1]),("y2",MY[2]),("y3",MY[3])])
testable.extend([("z0",MZ[0]),("z1",MZ[1]),("z2",MZ[2]),("z3",MZ[3])])

mv=MX[0]
mkmov(mv)
curr=list([FACES[k] for k in m])
print ([a==b for a,b in zip(ori,curr)].count(True))
for exchange in [(a,b) for a,b in zip(ori,curr) if a!=b]:
	print(exchange)
# ~ exit()
pathcode=""
USELESS=set()
record=0
sols={}
while True:
	code,tm=ch(testable)
	pathcode+=code
	# ~ print(pathcode)
	mkmov(tm)
	curr=list([FACES[k] for k in m])
	good=[a==b for a,b in zip(ori,curr)].count(True)
	# ~ print(good)
	if good==96:
		USELESS.add(pathcode)
		before=len(USELESS)
		keepgoing=True
		while keepgoing:
			# ~ print("useless\n",USELESS)
			for k in list(USELESS):
				for z in list(USELESS):
					USELESS.add(z.replace(k,""))
			if len(USELESS)==before:
				keepgoing=False
			else:before=len(USELESS)
	elif good>=record:
		record=good
		# ~ print(pathcode)
		print(good)
		keepgoing=True
		oripath=pathcode
		while keepgoing:
			# ~ print("simplifying")
			for k in USELESS:
				oripath=pathcode
				pathcode=pathcode.replace(k,"")
			if oripath==pathcode:keepgoing=False
		print(pathcode)
		# ~ input()
		if good in sols:
			if pathcode not in sols[good]:
				sols[good].add(pathcode)
				# ~ print(sols[good])
		else:
			sols[good]=set()
			sols[good].add(pathcode)
		# ~ input()
		# ~ pathcode=""
		# ~ for f in m:FACES[f]=f
		for exchange in [(a,b) for a,b in zip(ori,curr) if a!=b]:
			print(exchange)
		same_face=0
		for exchange in [(a,b) for a,b in zip(ori,curr) if a!=b]:
			a,b=exchange
			same_face+=[x*y for x,y in zip(a,b)].count(16)
		if same_face >0:
			print(pathcode)
			# ~ input(same_face)
	if len(pathcode)>1000:
		pathcode=""
		for f in m:FACES[f]=f
		
	
