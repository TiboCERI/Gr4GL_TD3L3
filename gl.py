#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement

def filtre(src,dst,element):
		titre = element.replace('.txt','').replace('_',' ') 		# on remplace les underscore par des espaces et on enleve l'extension du fichier 
		dst.write("Nom du pdf : "+titre+"\n")				 		# on ecrit le nom du pdf dans le fichier de destination (premiere ligne)					
		for i in range(2000,2019) :								
			if str(i) in titre :
				annee = str(i)	
		dst.write("Titre : "+  titre.split(annee)[1] + "\n")  		# on ecrit le titre du pdf dans le fichier de destination (deuxieme ligne)
		txt = src.read()											# lecture du fichier dans une variable string
		if "ABSTRACT" in txt :										# blocs de conditions pour identifier le début du résumé  
			debut = txt.split("ABSTRACT",1)						
								
		elif "Abstract" in txt :
			debut = txt.split("Abstract",1)
		
		fin="1"
		if "Keywords" in txt :										# blocs de conditions pour identifier la fin du résumé
			fin="Keywords"
			
		elif "Index" in txt :
			fin="Index"
		
		a1 = debut[1].split(fin)
		a2 = a1[0].split("\n")
		dst.write("Resumé : ")
		for i in range(0,len(a2)) :									# ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
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
        t = "{}/tmp".format(sys.argv[1])
        shutil.rmtree(t)
    else:
        print( "L'argument n'éxiste pas ou n'est pas un répertoire !")
        sys.exit(2)
        
