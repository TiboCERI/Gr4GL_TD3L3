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
    s = []
    s.append(arg)
    s.append("/result")
    result = ''.join(s)
    if os.path.exists(result):
       shutil.rmtree(result)
    os.mkdir(result)

    f = []
    f.append(arg)
    f.append("/tmp")
    tmp = ''.join(f)
    for element in os.listdir(tmp):
        if element.endswith('.txt'):
            a = "../result/"
            source = open(element,"r")
            destination = open(a+element, "w")
            filtre(source,destination)
            source.close()
            destination.close()


def pdf(arg):
    s = []
    s.append(arg)
    s.append("/tmp")
    tmp = ''.join(s)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    a = []
    for element in os.listdir(arg):
        if element.endswith('.pdf'):
            print(os.getcwd())
            a.append("pdf2txt -o -p[1] ")
            a.append(arg)
            a.append("/tmp/")
            a.append(element)
            a.append(".txt " )
            a.append(arg)
            a.append("/")
            a.append(element)
            
            sp.Popen(''.join(a))
          #  sp.run(["pdf2txt","-o" ,arg,"/tmp/",element, ".txt ", arg,element])


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
        