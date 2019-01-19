#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement
import xml.etree.ElementTree as ET #XML
from lxml import etree #XML

def Resume(Content):
    if "ABSTRACT" in Content :                                      # blocs de conditions pour identifier le début du résumé  
        debut = Content.split("ABSTRACT",1)                     
                                
    if "Abstract" in Content :
        debut = Content.split("Abstract",1)
    
    fin="1"
    if "Keywords" in Content :                                      # blocs de conditions pour identifier la fin du résumé
        fin="Keywords"
            
    elif "Index" in Content :
        fin="Index"
    try:
        debut
    except NameError:
        return "erreur"
    else:
        a1 = debut[1].split(fin)
        a2 = a1[0].split("\n")
        a = ''.join(a2)
        return a

def Introduction(Content):
    if "Introduction" in Content :
        debut = Content.split("Introduction\n",1)
        if "Mikolov" in Content:
            fin = "2 "
        else:
            fin = "2\n"
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "I. I NTRODUCTION" :
        debut = Content.split("I. I NTRODUCTION\n",1)
        fin = "II."
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[0].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "INTRODUCTION" :
        debut = Content.split("INTRODUCTION\n",1)
        if "Naive" in Content:
            fin = "2."
        else :
            fin = "2\n"
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a


def Conclusion(Content):
    if "Conclusion" in Content:
        debut = Content.split("Conclusion",1)
        if "Acknowledgments" in Content:
            fin= "Acknowledgments"
        elif "Acknowledgements" in Content:
            fin= "Acknowledgements"
        else:
            fin= "References\n"
        
        try:
            debut
            fin
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "VI. C ONCLUSIONS AND F UTURE W ORK" in Content:
        debut = Content.split("VI. C ONCLUSIONS AND F UTURE W ORK",1)

        fin= "ACKNOWLEDGMENT"

        try:
            debut
            fin
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "CONCLUSION" in Content:
        debut = Content.split("CONCLUSION",1)
        if "ACKNOWLEDGMENT" in Content:
            fin= "ACKNOWLEDGMENT"
        else:
            fin= "REFERENCES\n"
        
        try:
            debut
            fin
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
            
    return "erreur"

def Corps(Content):
    if "Introduction" in Content:
        debut = Content.split("Introduction",1)
        if "Mikolov" in Content:
            deb = "2 "
        else : 
            deb = "2\n"
        debut1 = debut[1].split(deb,1)
        fin = "Conclusion"
        try:
            debut1
        except NameError:
            return "erreur"
        else:
            a=debut1[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "I. I NTRODUCTION" :
        debut = Content.split("I. I NTRODUCTION\n",1)
        deb = "II. R ELATED W ORK"
        fin = "VI. C ONCLUSIONS AND F UTURE W ORK"
        debut1 = debut[1].split(deb,1)
        a=debut1[1].split(fin)
        a1=a[0]
        a = ''.join(a1)
        return a
    if "INTRODUCTION" in Content:
        debut = Content.split("INTRODUCTION",1)
        if "Naive" in Content:
            deb = "2."
        elif "Furui" in Content:
            deb = "II."
        else :
            debut = "2\n"
        debut1 = debut[1].split(deb,1)
        fin = "CONCLUSION"
        try:
            debut1
        except NameError:
            return "erreur"
        else:
            a=debut1[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    return "erreur"

def Discussion(Content):
    if "Acknowledgments" in Content:
        debut = Content.split("Acknowledgments",1)
        fin="References"
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "Acknowledgements" in Content:
        debut = Content.split("Acknowledgements",1)
        fin="References"
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    if "ACKNOWLEDGMENT" in Content:
        debut = Content.split("ACKNOWLEDGMENT",1)
        fin="REFERENCES"
        try:
            debut
        except NameError:
            return "erreur"
        else:
            a=debut[1].split(fin)
            a1=a[0]
            a = ''.join(a1)
            return a
    return "Pas de Discussion"

def Auteur(Content,titre):
    texte = Content.lower()
    titre2 = titre.split(" ")
    #print(titre2)
    mot = titre2[len(titre2)-2]+" "+titre2[len(titre2)-1]
    mot = mot.lower()
    if mot in texte :
        auteur = texte.split(mot)
        auteur2 = auteur[1].split("abstract",1)
        enligne = auteur2[0].replace('\n',"  ;  ")
        return enligne
    return "erreur"

def Titre(Content,titre):
    aut = Auteur(Content,titre)
    title = Content.split(aut)
    return titre

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
    if "[1]" in normalContent:
        contentOnLine = normalContent.replace(".\n","  ;  ").replace("\n"," ")
        contentOnLine = contentOnLine.replace(";", "\n")
        return contentOnLine
    elif "(2013)" in normalContent:
        normalContent = normalContent.replace("\n"," ")
        for i in range(1900,2020):
            if str(i) in normalContent:
                a = "("+str(i)+")"
                b = "("+str(i)+")\n"
                
                normalContent = normalContent.replace(a, b)
        return normalContent
    else:
        normalContent = normalContent.replace("\n"," ")
        for i in range(1900,2020):
            if str(i) in normalContent:
                a = str(i)+"."
                b = str(i)+".\n"

                
                normalContent = normalContent.replace(a, b)
        return normalContent
    

def filtre(src,dst,element):
    #-----------Nom du PDF-----------
        print(element)
        titre = element.replace('.txt','').replace('_',' ')         # on remplace les underscore par des espaces et on enleve l'extension du fichier 
        dst.write("Nom du pdf : "+titre+"\n")   
        txt = src.read()
        titre2 = titre
    #-----------Titre-----------                                    # on ecrit le nom du pdf dans le fichier de destination (premiere ligne)                    
        for i in range(2000,2019) :                             
            if str(i) in titre :
                annee = str(i)  
        try:
            annee
        except NameError:
            dst.write("titre may not found")
        else:
            titre2 = titre.split(annee)[1]
        if "Rouge" in titre :
            titre1 = txt.split("ROUGE:")
            titre2 = titre1[1].split("\n")[0]
            dst.write("\n\n\nTitre : "+  titre2 + "\n")
        elif "naive bayes" in titre:
            titre1 = txt.split("\n")
            titre2 = titre1[0]
            dst.write("\n\n\nTitre : "+  titre2 + "\n")
        else:  
            dst.write("\n\n\nTitre : "+  titre2 + "\n")       # on ecrit le titre du pdf dans le fichier de destination (deuxieme ligne)      
    #-----------Résumé-----------                                   # lecture du fichier dans une variable string
        a2 = Resume(txt)
        dst.write("\n\n\nResumé : ")
        for i in range(0,len(a2)) :                                 # ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
            dst.write(a2[i])
    #----------Auteurs------------
        
        dst.write("\n\n\n"+"Auteur : "+Auteur(txt,titre2))      
    #----------Biblio-------------
        
        dst.write("\n\n\n"+"Biblio : "+Biblio(txt))

    #---------Intro--------------
        dst.write("\n\n\n"+"Introduction : "+Introduction(txt))
    #---------Corps--------------
        dst.write("\n\n\n"+"Corps : "+Corps(txt))
    #---------Conclusion--------------
        dst.write("\n\n\n"+"Conclusion : "+Conclusion(txt))
    #---------Discussion--------------
        dst.write("\n\n\n"+"Discussion : "+Discussion(txt))    


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
            pdfToTextCommand = "pdftotext {1}/{2} {1}/tmp/{3}.txt".format(os.getcwd(),directoryPath, newFileName, fileNameWithouExt)
            # Executer la commande de conversion
            os.system(pdfToTextCommand)

def createXmlFile(src,dst,title,rwt):
                
    filename = dst+rwt+".xml"
    titre = title.replace('.txt','').replace('_',' ')
    txt = src.read()
    root = ET.Element("article")

    userelement = ET.SubElement(root,"preamble").text = titre
    for i in range(2000,2019) :

        if str(i) in titre:
            annee = str(i)  
    titre2 = titre.split(annee)[1]
    if "Rouge" in titre :
        titre1 = txt.split("ROUGE:")
        titre2 = titre1[1].split("\n")[0]
        userelement1 = ET.SubElement(root,"titre").text = titre2
    elif "naive bayes" in titre:
        titre1 = txt.split("\n")
        titre2 = titre1[0]
        userelement1 = ET.SubElement(root,"titre").text = titre2
    else:  
        userelement1 = ET.SubElement(root,"titre").text = titre2  
    userelement2 = ET.SubElement(root,"auteur").text = Auteur(txt, titre2)

    userelement3 = ET.SubElement(root,"abstract").text = Resume(txt)

    userelement4 = ET.SubElement(root,"introduction").text = Introduction(txt)
   
    userelement5 = ET.SubElement(root,"corps").text = Corps(txt)

    userelement6 = ET.SubElement(root,"conclusion").text = Conclusion(txt)

    userelement7 = ET.SubElement(root,"discussion").text = Discussion(txt)

    userelement8 = ET.SubElement(root,"biblio").text = Biblio(txt)
        
    tree= ET.ElementTree(root)
    tree.write(filename)        

def createFichierXml(arg) : 
    tmp = "{}/result".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    t = "{}/tmp".format(arg)
    for element in os.listdir(t):
        if element.endswith('.txt'):
            rwt = os.path.splitext(os.path.basename(element))[0]
            a = "{0}/result/".format(arg)
            s = "{0}/tmp/".format(arg)
            source = open(s+element,"r")  
            createXmlFile(source,a,element,rwt)
            source.close()


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
print("*       Welcome to PDF To TXT          *")
print("***************************************" + bcolors.ENDC)

# S'assurer que notre programme reçois le bon nombre d'argument 
# le premier argument est le nom de notre script python
# le deuxième argument est le répértoire content l'ensemble des fichiers pdf à convertir.
# le troisiéme argument est pour choisir le type de sortie soit txt ou xml

if len(sys.argv) != 3: 
    print(bcolors.FAIL + "Ooops nombre d'arguments incorrect" + bcolors.ENDC)
    print("Merci de passer en paramètre le dossier contenant les fichier pds à convertir.")
    print("et le type de sortie :")
    print(bcolors.OKBLUE+"soit -t pour un répertoire en format texte ."+bcolors.ENDC)
    print(bcolors.OKBLUE+"soit -x pour un répertoire en format xml."+ bcolors.ENDC)
    print("Exemple 1: " + bcolors.OKGREEN+"python3 gl.py chemin_vers_le_dossier -t pour un fichier TXT" + bcolors.ENDC)
    print("Exemple 2: " + bcolors.OKGREEN+"python3 gl.py chemin_vers_le_dossier -x pour un fichier XML" + bcolors.ENDC)
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
    # Verifier si le type de sortie est égale a txt
    if sys.argv[2] == '-t':
        # Début de la conversion
        print("Conversion pdf to txt")
        print ("Conversion des fichier du répértoire " + directory)
        pdf(directory)  
        transmog(directory)
        t = "{}/tmp".format(directory)
        #shutil.rmtree(t) 
    # Verifier si le type de sortie est égale a xml
    elif sys.argv[2] == '-x':
        # Début de la conversion
        print("Conversion pdf to xml")
        print ("Conversion des fichier du répértoire " + directory)
        pdf(directory)
        createFichierXml(directory) 
        t = "{}/tmp".format(directory)
        shutil.rmtree(t) 
    # Terminer le programme si l'argument de type de sortie n'égale ni à txt ni à xml 
    else :
        print(bcolors.FAIL + "Ooops le type de sortie est inconnue" + bcolors.ENDC)
        sys.exit(2)