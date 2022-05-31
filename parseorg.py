#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
fn= sys.argv[1]
cmd="""zcat %s |sed -n -e "/^LOCUS/p" -e "/^  ORGANISM/,/^REFERENCE/ p" """
z=os.popen(cmd%fn)
l=z.readline().strip()
Okay=["Eukaryota","Bacteria","Viruses","Archaea","other sequences","unclassified sequences","cellular organisms","Unclassified"]
rep=list("""()/'"@+:""")
todo=set()
LOC={}
while l:
	if l.startswith("LOCUS"):locus=l.split()[1]
	elif l.startswith("ORGANISM"):OL=[]
	elif l.startswith("REFERENCE"):
		phyl=" ".join(OL)
		if not [phyl.startswith(ok) for ok in Okay].count(True):
			print(locus,phyl)
			while not [phyl.startswith(ok) for ok in Okay].count(True):
				print(phyl)
				OL=OL[1:]
				phyl=" ".join(OL)
		for c in rep:
			phyl=phyl.replace(c,"_")
		phyl=phyl.replace("; ","/")
		phyl=phyl.replace(" ","_")
		phyl="/data/org/"+phyl[:-1]
		# ~ print(phyl)
		todo.add(phyl)
		if phyl in LOC:LOC[phyl].append(locus)
		else:LOC[phyl]=[locus]
	else:OL.append(l)
	l=z.readline().strip()
print("making %i directories"%len(LOC))
for p in todo:
	os.system("mkdir -p %s"%p)
	gbfn="%s/gb"%p
	gbfile=open(gbfn,"a")
	gbfile.write("\n".join(LOC[p]))
	gbfile.write("\n")
	gbfile.close()
	os.system("sort -u -o %s %s"%(gbfn,gbfn))
	
