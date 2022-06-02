#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from random import randint as ri
import numpy as np
n=10
g=np.random.randint(0,20,(n,n))

for l in g:print(l)
print()
import itertools as it
reci=0
recs=n*n*21
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
	zeroes=np.count_nonzero(x==0,axis=1)
	print(zeroes)
	while zeroes.any():
		m=zeroes[np.where(zeroes>=1)].min()
		print(m,zeroes)
		rownb=np.where(zeroes==m)[0][0]
		print("fiddling with row :",rownb)
		column=np.where(x[rownb]==0)[0][0]
		print ("fiddling at column :",column)
		x[rownb,column]=1000
		x[rownb][np.where(x[rownb]==0)]=-1000
		x[:,column][np.where(x[:,column]==0)]=-1000
		print(x)
		zeroes=np.count_nonzero(x==0,axis=1)
		print(zeroes)
		# ~ input()
	squared=np.count_nonzero(x==1000)
	print("squared :",squared)
	if squared != n:
		tl=np.count_nonzero(x==1000,axis=1)
		tl=np.where(tl==0)[0]
		print("TL :",tl)
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
			# ~ input()
		remain=x[tl,][:,[c for c in range(n) if c not in tc]]
		print(remain)
		print(remain.min())
	# ~ x[(0,1,2),][:,(3,4)]

# ~ print(reci,si)
# ~ print(recs,ss)
g=g.max()-g
a=g.min(axis=0)
g=g-a
print(g)
a=g.min(axis=1)
g=g.T-a
g=g.T
print()
print(g)
zeroes=np.count_nonzero(g==0,axis=1)
print (zeroes)
mark()
