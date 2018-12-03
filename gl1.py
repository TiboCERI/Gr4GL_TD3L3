#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys      #argument 
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement
import subprocess as sp #commande 
import re       # RegEx

def filtre(src,dst,element):
    dst.write(element.replace('.pdf.txt','').replace('_',' '))
    txt = ''
    for ligne in src:
        txt += ligne
    str = re.search('Abstract(.*)$/gs', src)
    str.group()
    dst.write(str)


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
    shutil.rmtree(t)

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
            print(os.getcwd())
            print(element)
            a ="pdftotext -f 1 {1}/{2} {1}/tmp/{2}.txt".format(os.getcwd(),arg, element)
            os.system(a)
           # sp.check_call(["pdftotext",  "-f 1", "{0}/{1}".format(arg, element)])
          #  sp.run(["pdf2txt","-o" ,arg,"/tmp/",element, ".txt ", arg,element])
        #    a = "pdf2txt -p[1] '{0}/{1}/{2}' > {0}/{1}/tmp/{2}.txt".format(os.getcwd(),arg, element)


if len(sys.argv) != 2:
    print("Un seul argument attendu !")
    print(sys.argv)
    sys.exit(2)
else:
    current = os.getcwd()
    if os.path.exists(sys.argv[1]) & os.path.isdir(sys.argv[1]):
       # os.chdir(sys.argv[1])
        pdf(sys.argv[1])
        transmog(sys.argv[1])
       # sp.Popen("rm tmp")
    else:
        #print(sys.argv[1])
        print( "L'argument n'éxiste pas ou n'est pas un répertoire !")
        sys.exit(2)
        