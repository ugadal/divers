#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import numpy as np
import matplotlib.pyplot as plt
import csv
# ~ import pandas as pd
fn="/data/yeast/SraRunTable.txt"
genotypefile=open(fn)
csv=csv.reader(genotypefile)
genotype=[row[18] for row in csv][1:]
genotype=[s.replace('\\,','') for s in genotype]
genotype=[s.replace('knockout','') for s in genotype]
genotype=[s.replace('HIS3 ','H') for s in genotype]
genotype=[s.replace('LEU2 ','L') for s in genotype]
genotype=[s.replace('URA3 ','U') for s in genotype]
genotype=[s.replace('MET15 ','M') for s in genotype]
genotype=[s.replace('PROTOTROPH','P') for s in genotype]

con=pymysql.connect(database="levure",password="xxxxxx")
c=con.cursor()
c.execute("select distinct name from gc")
gene_names=np.array(c.fetchall())[:,0]
c.execute("select distinct exp from gc")
exp_names=np.array(c.fetchall())[:,0]
simp_names=[s.replace("ERR10951","") for s in exp_names]
print(gene_names)
print(exp_names)
Labels={}
for k,v in zip(exp_names,genotype):
	Labels[k]=v
C=[]
for exp in exp_names:
	c.execute("select nbr from gc where exp=%s",exp)
	C.append(np.array(c.fetchall())[:,0])
z=np.c_[C]	
# ~ z=z[:,100:150]
sbe=z.sum(axis=1)
scaled=z.T/sbe*1000000
# ~ scaled=scaled.T
scaled=scaled.T-scaled.mean(axis=1)
scaled=scaled.T
cov=np.cov(scaled)
val,vec=np.linalg.eigh(cov)
nref=vec[:,(-1,-2)]
NP=scaled.T@nref
NP=NP.T
plt.scatter(NP[0],NP[1])
for t,x,y in zip(Labels.values(),NP[0],NP[1]):
	plt.annotate(t,(x,y))
TRX={}
TRY={}
for k in set(Labels.values()):
	TRX[k]=[]
	TRY[k]=[]
for t,x,y in zip(Labels.values(),NP[0],NP[1]):
	TRX[t].append(x)
	TRY[t].append(y)
for k in TRX.keys():
	tx=TRX[k]
	ty=TRY[k]
	print(tx)
	tx.append(tx[0])
	ty.append(ty[0])
	plt.plot(tx,ty,color="g")
plt.show()
