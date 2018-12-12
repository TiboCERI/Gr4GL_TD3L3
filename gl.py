#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement

def filtre(src,dst,element):
        # on remplace les underscore par des espaces et on enleve l'extension du fichier 
		titre = element.replace('.txt','').replace('_',' ')
        # on ecrit le nom du pdf dans le fichier de destination (premiere ligne) 		
		dst.write("Nom du pdf : "+titre+"\n")				 							
		for i in range(2000,2019) :								
			if str(i) in titre :
				annee = str(i)	
        # on ecrit le titre du pdf dans le fichier de destination (deuxieme ligne)
		dst.write("Titre : "+  titre.split(annee)[1] + "\n") 
        # lecture du fichier dans une variable string 		
		txt = src.read()
        # blocs de conditions pour identifier le début du résumé  											
		if "ABSTRACT" in txt :										
			debut = txt.split("ABSTRACT",1)						
								
		elif "Abstract" in txt :
			debut = txt.split("Abstract",1)
		
		fin="1"
        # blocs de conditions pour identifier la fin du résumé
		if "Keywords" in txt :										
			fin="Keywords"
			
		elif "Index" in txt :
			fin="Index"
		
		a1 = debut[1].split(fin)
		a2 = a1[0].split("\n")
		dst.write("Resumé : ")
        # ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
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


def pdf(directoryPath):
    # Faire une purge du répértoire temporaire à l'intérieur du dossier passé
    # en paramètre lorsqu'il existe
    tmp = "{}/tmp".format(directoryPath)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    
    # Créer un dossier temporaire à l'intérieur du dossier passé en paramètres
    os.mkdir(tmp)

    # Pour chaque fichier pdf ( se terminant par .pdf)
    for fileName in os.listdir(directoryPath):
        if fileName.endswith('.pdf'):
            # Récupérer le nom du fichier sans extension
            fileNameWithouExt = os.path.splitext(fileName)[0]
            # Créer un nom de fichier qui est le même que le fichier pdf
            # en remplacent les espace par des underscore
            newFileName = fileName.replace(' ','_')

            # renommer le fichier 
            os.rename("{0}/{1}".format(directoryPath,fileName), "{0}/{1}".format(directoryPath,newFileName))
            # créer la commande qui permet de faire la conversion
            pdfToTextCommand = "pdftotext -f 1 {1}/{2} {1}/tmp/{3}.txt".format(os.getcwd(),directoryPath, newFileName, fileNameWithouExt)
            # Executer la commande de conversion
            os.system(pdfToTextCommand)
          
            
    

# code des couleurs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
          
print(bcolors.HEADER + "***************************************")
print("*       Welcom to PDF To TXT          *")
print("***************************************" + bcolors.ENDC)

# S'assurer que notre programme reçois le bon nombre d'argument 
# le premier argument est le nom de notre script python
# le deuxième argument est le répértoire content l'ensemble des fichiers pdf à convertir.
if len(sys.argv) != 2: 
    print(bcolors.FAIL + "Ooops nombre d'arguments incorrect" + bcolors.ENDC)
    print("Merci de passer en paramètre le dossier contenant les fichier pds à convertir.")
    print("Exemple: " + bcolors.OKGREEN+"python3 gl.py chemin_vers_le_dossier" + bcolors.ENDC)
    sys.exit(2)
else:
    # Récupérer le répértoire courant ( cwd : current working directory )
    current = os.getcwd()
    directory = sys.argv[1]

    # Terminer le programme si l'argument passé en paramètre n'existe pas
    if not os.path.exists(directory):
        print(bcolors.FAIL + "L'argument passé en paramètre n'existe pas." + bcolors.ENDC)
        sys.exit(2)
    
    # Terminer le programme si le l'argument passé en n'est pas un dossier
    if not os.path.isdir(directory):
        print(bcolors.FAIL + "L'argument passé en paramètre n'est pas un dossier." + bcolors.ENDC)
        sys.exit(2)
    
    # Début de la conversion
    print ("Conversion des fichier du répértoire " + directory)
    pdf(directory)	
    transmog(directory)
    t = "{}/tmp".format(directory)
    shutil.rmtree(t)   
