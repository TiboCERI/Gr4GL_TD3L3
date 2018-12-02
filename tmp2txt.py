#!/usr/bin/env python
import sys
import os
import subprocess as sp

def filtre(src,dst):
    for ligne in src:
        print(ligne)


def transmog():
    if exists("result"):
        sp.Popen("rm result")
    sp.Popen("mkdir result")
    for element in os.listdir('/tmp'):
        if element.endswith('.txt'):
            a = "../result/"
            source = open(element,"r")
            destination = open(a+element, "w")
            filtre(source,destination)
            source.close()
            destination.close()


def pdf(arg):
    sp.Popen("mkdir tmp")
    for element in os.listdir(arg):
        if element.endswith('.pdf'):
            a = "pdf2txt "
            a += element
            a += " > tmp/"
            a += element
            a += ".txt" 
            sp.Popen(a)


if sys.argv != 2:
    print "Un seul argument attendu !"
    sys.exit(2)
else:
    if exists(sys.argv[1]):
        pdf(sys.argv[1])
        transmog()
    else:
        sys.exit(2)
        