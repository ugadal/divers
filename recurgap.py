#!/usr/bin/env python
# -*- coding: utf-8 -*-
SH="ABCDE"
SV="ABe"
def H(l,c):
	if l==c==0:return 0
	if c==0:return -99999
	if l==0:return -9-c
	h=H(l,c-1)-1
	v=V(l,c-1)-10
	d=D(l,c-1)-10
	return max(h,v,d)
def V(l,c):
	if l==c==0:return  0
	if l==0:return -9999
	if c==0:return -9-l
	h=H(l-1,c)-10
	v=V(l-1,c)-1
	d=D(l-1,c)-10
	return max(h,v,d)
def D(l,c):
	if l==c==0:return 0
	if l*c==0:return -9999
	aah=SH[c-1]
	aav=SV[l-1]
	if aah==aav:score=5
	else:score=-5
	h=H(l-1,c-1)
	v=V(l-1,c-1)
	d=D(l-1,c-1)
	return max(h,v,d)+score
print(D(3,5))
print(H(3,5))
print(V(3,5))


