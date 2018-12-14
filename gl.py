#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement

def filtre(src,dst,element):
	#-----------Nom du PDF-----------
		titre = element.replace('.txt','').replace('_',' ') 		# on remplace les underscore par des espaces et on enleve l'extension du fichier 
		dst.write("Nom du pdf : "+titre+"\n")	
		txt = src.read()
	#-----------Titre-----------							 		# on ecrit le nom du pdf dans le fichier de destination (premiere ligne)					
		for i in range(2000,2019) :								
			if str(i) in titre :
				annee = str(i)	
		titre2 = titre.split(annee)[1]
		if "Rouge" in titre :
			titre1 = txt.split("ROUGE:")
			titre2 = titre1[1].split("\n")[0]
			dst.write("Titre : "+  titre2 + "\n")
		elif "naive bayes" in titre:
			titre1 = txt.split("\n")
			print(titre1)
			#titre2 = titre1[1].split("\n")
		else:  
			dst.write("Titre : "+  titre2 + "\n")  		# on ecrit le titre du pdf dans le fichier de destination (deuxieme ligne)
			
		
				
		
	#-----------Résumé-----------									# lecture du fichier dans une variable string
		a2 = Resume(txt)
		dst.write("Resumé : ")
		for i in range(0,len(a2)) :									# ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
			dst.write(a2[i])
			
	#----------Auteurs------------
		if "ROUGE:" in txt :
			dst.write("\n"+"Auteur : "+Auteur(txt,titre2))
		else :
			dst.write("\n"+"Auteur : "+Auteur(txt,titre2))
				
	#----------Biblio-------------
		
		dst.write("\n"+"Biblio : "+Biblio(txt))


def Resume(Content):
	if "ABSTRACT" in Content :										# blocs de conditions pour identifier le début du résumé  
		debut = Content.split("ABSTRACT",1)						
								
	if "Abstract" in Content :
		debut = Content.split("Abstract",1)
		
	fin="1"
	if "Keywords" in Content :										# blocs de conditions pour identifier la fin du résumé
		fin="Keywords"
			
	elif "Index" in Content :
		fin="Index"
		
	a1 = debut[1].split(fin)
	a2 = a1[0].split("\n")
	return a2



def Auteur(Content,titre):
	texte = Content.lower()
	titre2 = titre.split(" ")
	#print(titre2)
	mot = titre2[len(titre2)-2]+" "+titre2[len(titre2)-1]
	mot = mot.lower()
	if mot in texte :
		auteur = texte.split(mot)
		auteur2 = auteur[1].split("abstract",1)
		return auteur2[0]




def Biblio(normalContent):
	lowerContent = normalContent.lower()
	if " references" in lowerContent:
		indexFound = lowerContent.find("\nreferences\n")
	else:
		indexFound = lowerContent.find("references\n")
	if indexFound == -1 :
		return "bibliography not found"
	indexFound += len("references\n")
	normalContent = normalContent[indexFound:]
	indexFound = normalContent.find("\n\n");
	if indexFound == -1 :
		return "bibliography not found"
	normalContent = normalContent[:indexFound]
	return normalContent


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
            # créer la commande qui permet de 
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

    # Terminer le programme si le l'argument passé en paramètre n'existe pas
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
    #shutil.rmtree(t)   
