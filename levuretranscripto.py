#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

fn="/data/yeast/SraRunTable.txt"
genotypefile=open(fn)
csv=csv.reader(genotypefile)
exg=[(row[0],row[18]) for row in csv][1:]
exps=[a for a,b in exg]
genotype=[b for a,b in exg]
genotype=[s.replace('\\,','') for s in genotype]
genotype=[s.replace('knockout','') for s in genotype]
genotype=[s.replace('HIS3 ','H') for s in genotype]
genotype=[s.replace('LEU2 ','L') for s in genotype]
genotype=[s.replace('URA3 ','U') for s in genotype]
genotype=[s.replace('MET15 ','M') for s in genotype]
genotype=[s.replace('PROTOTROPH','P') for s in genotype]

genotypes=list(set(genotype))
genotypes.sort()
print(genotypes)

Labels={}
for geno in genotypes:
	Labels[geno]=[]
for geno,exp in zip(genotype,exps):
	Labels[geno].append(exp)
	Labels[geno].sort()
# ~ Manual correction
Labels["UM"]=["ERR1095171","ERR1095172","ERR1095182"]
Labels["M"]=["ERR1095184","ERR1095173","ERR1095187"]
Labels["LU"]=["ERR1095181","ERR1095185","ERR1095183"]
Labels["H"]=["ERR1095188","ERR1095189","ERR1095180"]
Labels["HU"]=["ERR1095178","ERR1095179","ERR1095190"]
Labels["HLM"]=["ERR1095153","ERR1095154","ERR1095168"]
Labels["LM"]=["ERR1095186","ERR1095169","ERR1095170"]
for geno in genotypes:
	print(geno,Labels[geno])

import pymysql
import numpy as np
import matplotlib.pyplot as plt
con=pymysql.connect(host="big",database="levure",password="xxxxxx")
c=con.cursor()

C=[]
ylabl=[]
genolbl=[]
explbl=[]
ccc=-1
for geno in genotypes:
	for exp in Labels[geno]:
		ccc+=1
		print(ccc,geno,exp)
		ylabl.append(geno.ljust(6)+exp)
		genolbl.append(geno)
		explbl.append(exp)
		c.execute("select nbr from gc where exp=%s",exp)
		C.append(np.array(c.fetchall())[:,0])
z=np.c_[C]	
# ~ z=z[:,100:150]

sbe=z.sum(axis=1)
scaled=z.T/sbe*1000000
print(sbe.mean())
print(sbe,max(sbe),min(sbe))
# ~ input
scaled=scaled.T-scaled.mean(axis=1)
scaled=scaled.T

# ~ corr matrix heatmap
cov=np.cov(scaled.T)

fig, ax = plt.subplots(1,1)
img = ax.imshow(z)
x_label_list = ['A1', 'B1', 'C1', 'D1']
ax.set_xticks(range(0,48,3))
ax.set_yticks(range(0,48))
ax.set_xticklabels(genotypes)
ax.set_yticklabels(ylabl)
plt.imshow(cov, cmap='jet')
plt.show()

# ~ pca
cov=np.cov(scaled)
val,vec=np.linalg.eigh(cov)
nref=vec[:,(-1,-2)]
NP=scaled.T@nref
NP=NP.T
plt.scatter(NP[0],NP[1])
for t,x,y in zip(genolbl,NP[0],NP[1]):
	plt.annotate(t,(x,y))
TRX={}
TRY={}
for k in genotypes:
	TRX[k]=[]
	TRY[k]=[]
for t,x,y in zip(genolbl,NP[0],NP[1]):
	TRX[t].append(x)
	TRY[t].append(y)
for k in genotypes:
	tx=TRX[k]
	ty=TRY[k]
	print(tx)
	tx.append(tx[0])
	ty.append(ty[0])
	plt.plot(tx,ty,color="g")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA projection of 48 experiments triangle-linked by proposed genotype")
plt.show()
