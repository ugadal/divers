#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import glob
os.chdir("/data/org")
# ~ def issum():
	
def up():
	os.chdir("..")
def getdirs():
	r=[]
	for it in os.scandir():
		if it.is_dir(): r.append(it)
	return r
while not os.getcwd()=="/data":
	#are there branches
	if getdirs(): 
		print("subsdirs")
	# ~ elif 
	exit()
