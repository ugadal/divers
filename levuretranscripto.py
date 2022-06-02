#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

Labels={}

import pymysql
con=pymysql.connect(host="big",database="levure",password="xxxxxx")
c=con.cursor()
c.execute("select distinct exp from gc")
exps=[exp for exp, in c.fetchall()]
genotype={}
for exp in exps:genotype[exp]=""
tags=list("UMLH")
genecodes=("YEL021W","YLR303W","YCL018W","YOR202W")
for t,g in zip(tags,genecodes):
	c.execute("select exp from gc where name=%s order by nbr",g)
	res=c.fetchall()
	for exp, in res[:24]:
		genotype[exp]+=t
for exp in exps:
	t=list(genotype[exp])
	t.sort()
	t="".join(t)
	if t=="":t="P"
	genotype[exp]=t
	print(exp,genotype[exp])
genotypes=list(set(genotype.values()))	
genotypes.sort()
for geno in genotypes:
	Labels[geno]=list([k for k,v in genotype.items() if v==geno])
for k,v in Labels.items():print(k,v)
# ~ exit()
import numpy as np
import matplotlib.pyplot as plt
# ~ con=pymysql.connect(host="big",database="levure",password="xxxxxx")
# ~ c=con.cursor()

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
print(len(z))
sbe=z.sum(axis=1)
scaled=z.T/sbe*1000000
# ~ print(sbe.mean())
# ~ print(sbe,max(sbe),min(sbe))
# ~ input
scaled=scaled.T-scaled.mean(axis=1)
scaled=scaled.T

# ~ fo=open("D.csv","w")
# ~ co=csv.writer(fo)
# ~ co.writerows(D)

fo=open("scaled.csv","w")
co=csv.writer(fo)
co.writerows(scaled)
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
print (val)
nref=vec[:,(-1,-2)]
fo=open("PCs.csv","w")
co=csv.writer(fo)
co.writerows(nref)
# ~ fo=open("eigenvals.csv","w")
# ~ co=csv.writer(fo)
# ~ co.writerows(val)
# ~ exit()
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
