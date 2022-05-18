#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Rub4x4.py
#  
import numpy as np
D=[]
for f in range(4):
	D.append([0]*4+[1]*4+[2]*4)
	
for c in range(3,6):
	for f in range(4):
		D.append([" "]*4+[c]*4+[" "]*4)

M=np.matrix(D)
M=M.reshape(16,12)
print (M)
fg=np.ix_(range(4),range(4)) #gauche
fd=np.ix_(range(4),range(8,12)) #droite
ft=np.ix_(range(4),range(4,8)) #dessus
ff=np.ix_(range(4,8),range(4,8)) #devant
fb=np.ix_(range(8,12),range(4,8)) #dessous
fa=np.ix_(range(12,16),range(4,8)) #arrière
print(M[fg])
print(M[fd])
def f(c):
	if c==1:M[fg]=np.rot90(M[fg])
	if c==4:
		M[fd]=np.rot90(M[fd])
		M[fd]=np.rot90(M[fd])
		M[fd]=np.rot90(M[fd])
	tc=np.ix_(range(16),[c+3])
	M[tc]=np.roll(M[tc],-4,axis=0)
	print(M[tc])
	print(M)
def t(c):
	if c==1:
		M[ff]=np.rot90(M[ff])
		M[ff]=np.rot90(M[ff])
		M[ff]=np.rot90(M[ff])
	if c==4:
		M[fa]=np.rot90(M[fa])
	tc=np.ix_(range(16),[c+3])
	# ~ M[tc]=np.roll(M[tc],4,axis=0)
	# ~ print(M[tc])
	print(M)
f(1)
t(4)
