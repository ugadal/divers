#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from random import randint as ri
import numpy as np
n=5
# ~ g=np.random.randint(0,20,(n,n))
def mkgrid():
	g=np.random.randint(0,20,(n,n))
	print(g)
	g=g.max()-g
	print(g)
	a=g.min(axis=1)
	g=g.T-a
	g=g.T
	a=g.min(axis=0)
	g=g-a
	print(g)
	# ~ zeroes=np.count_nonzero(g==0,axis=1)
	# ~ print (zeroes)
	return g
# ~ for l in g:print(l)
# ~ print()
import itertools as it
reci=0
recs=n*n*21
si=""
ss=""
# ~ for c in it.permutations (list(range(n))):
	# ~ ttl=sum([g[l,c] for l,c in zip (range(n),c)])
	# ~ if ttl >reci:
		# ~ reci=ttl
		# ~ si=(c,[g[l,c] for l,c in zip (range(n),c)])
	# ~ if ttl <recs:
		# ~ recs=ttl
		# ~ ss=(c,[g[l,c] for l,c in zip (range(n),c)])

def mark():
	x=g.copy()
	zeroes=np.count_nonzero(x==0)
	print(zeroes)
	notfound=True
	cycles=0
	while zeroes:
		cycles+=1
		notfound=False
		lc=np.count_nonzero(x==0,axis=1)
		cc=np.count_nonzero(x==0,axis=0)
		full=np.append(lc,cc)
		m=full[np.where(full>0)].min()
		print(full,m)
		if m in lc:
			row=np.where(lc==m)[0][0]
			col=np.where(x[row]==0)[0][0]
			print("row")
		else:
			col=np.where(cc==m)[0][0]
			row=np.where(x[:,col]==0)[0][0]
			print("col")
		print(row,col)
		x[row,col]=1000
		x[row][np.where(x[row]==0)]=-1000
		x[:,col][np.where(x[:,col]==0)]=-1000
		print(x)
		zeroes=np.count_nonzero(x==0)
	squared=np.count_nonzero(x==1000)
	if squared==n:
		print(x)
		print("solved")
		exit()
	
	print("squared :",squared)
	tl=np.count_nonzero(x==1000,axis=1)
	tl=np.where(tl==0)[0]
	print("TL :",tl)
	input()
	col=(x[tl,])
	print(col)
	tc=np.count_nonzero(col==-1000,axis=0)
	tc=np.where(tc>=1)[0]
	print("TC:",tc)
	print(x[:,tc])
	changed=True
	while changed:
		changed=False
		ntl=np.count_nonzero(x[:,tc]==1000,axis=1)
		ntl=np.where(ntl>=1)[0]
		print("ntl:",ntl)
		for l in ntl:
			if l not in tl:
				tl=np.append(tl,l)
				tl.sort()
				changed=True
		col=(x[tl,])
		print(col)
		ntc=np.count_nonzero(col==-1000,axis=0)
		ntc=np.where(ntc>=1)[0]
		print("ntc",ntc)
		for c in ntc:
			if c not in tc:
				tc=np.append(tc,c)
				tc.sort()
				changed=True
		print("TL:",tl)
		print("TC:",tc)
		print(x[:,tc])
		print(changed)
		print(x)
		input()
		# ~ remain=x[tl,][:,[c for c in range(n) if c not in tc]]
		# ~ print(remain)
		# ~ print(remain.min())
		# ~ m=remain.min()
		# ~ x[np.where(x==1000)]=0
		# ~ x[np.where(x==-1000)]=0
		# ~ for l in tl:
			# ~ for c in range(n):
				# ~ if c not in tc:x[l,c]-=m
		# ~ for c in tc:
			# ~ for l in range(n):
				# ~ if l not in tl:x[l,c]+=m
		# ~ print(x[tl,][:,[c for c in range(n) if c not in tc]])
		# ~ print(x)
		# ~ zeroes=np.count_nonzero(x==0,axis=1)
		# ~ notfound=True

	# ~ x[(0,1,2),][:,(3,4)]

while True:
	print("="*50)
	g=mkgrid()
	mark()
# ~ g=g.max()-g
# ~ a=g.min(axis=0)
# ~ g=g-a
# ~ print(g)
# ~ a=g.min(axis=1)
# ~ g=g.T-a
# ~ g=g.T
# ~ print()
# ~ print(g)
# ~ zeroes=np.count_nonzero(g==0,axis=1)
# ~ print (zeroes)
# ~ mark()
# ~ print(reci,si)
print(recs,ss)
