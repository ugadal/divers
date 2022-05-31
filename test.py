#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from random import choice as ch
from time import sleep
def MX(k):
	p=[-2,-1,1,2][k]
	def z():
		moving=list([(x,y,z) for x,y,z in m if x==p])
		vals=list(FACES[p] for p in moving)
		pos=list([(x,z,-y) for x,y,z in moving])
		for k,v in zip(pos,vals):FACES[k]=v
	return z
def MY(k):
	p=[-2,-1,1,2][k]
	def z():
		moving=list([(x,y,z) for x,y,z in m if y==p])
		vals=list(FACES[p] for p in moving)
		pos=list([(z,y,-x) for x,y,z in moving])
		for k,v in zip(pos,vals):FACES[k]=v
	return z
def MZ(k):
	p=[-2,-1,1,2][k]
	def z():
		moving=list([(x,y,z) for x,y,z in m if z==p])
		vals=list(FACES[p] for p in moving)
		pos=list([(y,-x,z) for x,y,z in moving])
		for k,v in zip(pos,vals):FACES[k]=v
	return z
MOVES=[]
MOVES.extend([("x%i"%p,MX(p)) for p in range(4)])
MOVES.extend([("y%i"%p,MY(p)) for p in range(4)])
MOVES.extend([("z%i"%p,MZ(p)) for p in range(4)])
v=[-2,-1,1,2]
m=[(2,y,z) for y in v for z in v]
m.extend([(-2,y,z) for y in v for z in v])
m.extend([(1,y,2) for y in v])
m.extend([(1,y,1) for y in [-2,2]])
m.extend([(1,y,-1) for y in [-2,2]])
m.extend([(1,y,-2) for y in v])
m.extend([(-1,y,2) for y in v])
m.extend([(-1,y,1) for y in [-2,2]])
m.extend([(-1,y,-1) for y in [-2,2]])
m.extend([(-1,y,-2) for y in v])
FACES={}
for f in m:FACES[f]=f
ori=list(FACES.values())
def ok():
	oknum=[i==j for i,j in zip (FACES.values(),ori)].count(True)
	return oknum
def rep():
	for i,j in zip (FACES.values(),ori):
		if i!=j:print(j,i)
print(ok())
x1=MX(1)
x2=MX(2)
y1=MY(1)
x1()
# ~ y1()
# ~ y1()
x1()
y1()
x2()
y1()
y1()
y1()
x1()
x1()
x1()
y1()
x2()
x2()
x2()
y1()
y1()
y1()
# ~ x1()
print(ok())
print(FACES[(-1,-2,2)])
rep()
exit()
# ~ MOVES[11][1]()
# ~ print(ok())
# ~ exit()
pathcode=""
USELESS=set()
record=0
sols={}
# ~ keymove=list(MOVES.keys())
while True:
	code,mv=ch(MOVES)
	pathcode+=code
	mv()
	# ~ print(pathcode)
	good=ok()
	# ~ print(good)
	# ~ exit()
	# ~ input()
	
	if good==56:
		if pathcode in USELESS:continue
		print(len(pathcode),good,pathcode,record,sols[record])
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
		print(USELESS)
		print(pathcode)
		sleep(5)
	elif good>=record:
		record=good
		# ~ print(pathcode)
		# ~ input()
		# ~ print(good)
		keepgoing=True
		oripath=pathcode
		while keepgoing:
			oripath=pathcode
			for k in USELESS:
				pathcode=pathcode.replace(k,"")
			if oripath==pathcode:keepgoing=False
		# ~ print(pathcode)
		# ~ input()
		if good in sols:
			if pathcode not in sols[good]:
				sols[good].add(pathcode)
				# ~ print(sols[good])
		else:
			sols[good]=set()
			sols[good].add(pathcode)
	previous=pathcode
	goon=True
	while goon:
		for z in USELESS:
			pathcode=pathcode.replace(z,"")
		if pathcode==previous:goon=False
		else:previous=pathcode
	if len(pathcode)>100:
		pathcode=""
		for f in m:FACES[f]=f
		
	
