#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement
import subprocess as sp #commande 
import re       # RegEx

def filtre(src,dst,element):
		dst.write("Nom du pdf : "+element.replace('.txt','').replace('_',' ')+"\n")
		titre = element.replace('.txt','').replace('_',' ')
		titre.split("20"*)
		txt = src.read()
		
		"""titre = ""
		for ligne in txt :
			if ligne == '\n' :
				break
			else:
				titre += ligne
		dst.write("Titre du pdf : "+titre+"\n")
		"""
		if "ABSTRACT" in txt :
			a0 = txt.split("ABSTRACT",1)
			
		
		elif "Abstract" in txt :
			a0 = txt.split("Abstract",1)
		
		k="1"
		
		if "Keywords" in txt :
			k="Keywords"
			
		elif "Index" in txt :
			k="Index"
		
		a1 = a0[1].split(k)
		a2 = a1[0].split("\n")
		dst.write("Resumé : ")
		for i in range(0,len(a2)) :
			dst.write(a2[i])
		
		
				
		
		
			
			
		
		
		
	


def transmog(arg):
    tmp = "{}/result".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    t = "{}/tmp".format(arg)
    for element in os.listdir(t):
        if element.endswith('.txt'):
			a = "{0}/result/".format(arg)
			s = "{0}/tmp/".format(arg)
			source = open(s+element,"r")
			destination = open(a+element, "w")	
			filtre(source,destination,element)
			source.close()
			destination.close()
	#shutil.rmtree(t)

def pdf(arg):
    tmp = "{}/tmp".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    for element in os.listdir(arg):
        if element.endswith('.pdf'):
            s = element.replace(' ','_')
            os.rename("{0}/{1}".format(arg,element), "{0}/{1}".format(arg,s))
    for element in os.listdir(arg):
        if element.endswith('.pdf'):
            el = element.replace('.pdf','')
            a ="pdftotext -f 1 {1}/{2} {1}/tmp/{3}.txt".format(os.getcwd(),arg, element,el)
            os.system(a)
          


if len(sys.argv) != 2:
    print("Un seul argument attendu !")
    print(sys.argv)
    sys.exit(2)
else:
    current = os.getcwd()
    if os.path.exists(sys.argv[1]) & os.path.isdir(sys.argv[1]):
        pdf(sys.argv[1])
        transmog(sys.argv[1])
    else:
        print( "L'argument n'éxiste pas ou n'est pas un répertoire !")
        sys.exit(2)
        
