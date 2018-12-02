#!/usr/bin/env python
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement
import subprocess as sp #commande 

def filtre(src,dst):
    for ligne in src:
        print(ligne)



def transmog(arg):
    tmp = "{}/result".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    t = "{}/tmp".format(arg)
    for element in os.listdir(t):
        if element.endswith('.txt'):
            a = "../result/"
            source = open(element,"r")
            destination = open(a+element, "w")
            filtre(source,destination)
            source.close()
            destination.close()


def pdf(arg):
    tmp = "{}/tmp".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    for element in os.listdir(arg):
        if element.endswith('.pdf'):
            print(os.getcwd())
            a = "pdf2txt -p[1] '{0}/{1}/{2}' > {0}/{1}/tmp/{2}.txt".format(os.getcwd(),arg, element)
            sp.Popen(a)
          #  sp.run(["pdf2txt","-o" ,arg,"/tmp/",element, ".txt ", arg,element])
        #    a = "pdf2txt -p[1] '{0}/{1}/{2}' > {0}/{1}/tmp/{2}.txt".format(os.getcwd(),arg, element)


if len(sys.argv) != 2:
    print("Un seul argument attendu !")
    print(sys.argv)
    sys.exit(2)
else:
    current = os.getcwd()
    if os.path.exists(sys.argv[1]):
       # os.chdir(sys.argv[1])
        pdf(sys.argv[1])
        transmog(sys.argv[1])
       # sp.Popen("rm tmp")
    else:
        sys.exit(2)
        