# Gr4GL_TD3L3 github : https://github.com/TiboCERI/Gr4GL_TD3L3
# the pdf converter 
### ******* version 4.0.0 *******
Ce programme vous permet de convertir un PDF en fichier TEXTE ou XML.
#### Authors:

-Nizar REZAIGUI (SCRUM Master) -----> Krs-ceri

-Thibaut CHASTELLIERE   -----> TiboCERI

-Florian FEUILLEPAIN  ------> FlorianFeuillepain

-Zinedine MAKHLOUF  ------> AngryTaiga

-Hafsa LAACHIRI   ------> hflaachiri

#### Prerequisites :
vous devez installez :
```console
lxml
pdftotext
```
#### Installing :
Pour installer lxml sous LINUX dans une fenetre de commande tapez :
````console
$ sudo apt-get install python3-lxml

````
Pour installer pdftotext sous LINUX dans une fenetre de commande tapez :
````console
$ sudo apt-get install poppler-utils

````

#### How to use :
Pour lancer le programme il suffit de mettre le dossier Papers et le fichier gl.py dans un même dossier,puis d'ouvrir le terminal à partir de ce dossier et de lancer le programme avec Papers en argument .

Tapez la commande suivante dans le console pour effectuer la conversion :

    ```console

    $ python3 gl.py Papers -t     \\ pdf to text

    $ python3 gl.py Papers -x     \\ pdf to xml

    ```
   
Les pdf traités se retrouve dans le dossier Papers/result.

Dans chaque pdf traité on a identifié : 
  -Le nom du fichier d’origine (dans une ligne)
  -Le titre du papier (dans une ligne)
  -Le résumé ou abstract de l’auteur 
  -L'auteur
  -La bibliographie 
  -La conclusion
  -La discussion



-Utilisation d'un executeur dans le programme permettant de lancer la commande 'pdftotext'



