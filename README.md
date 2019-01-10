# Gr4GL_TD3L3
# the pdf converter 
### ******* version 3.0.0 *******
Ce programme vous permet de convertir un PDF en fichier TEXTE ou XML.
#### Authors:
-Nizar REZAIGUI (SCRUM Master)

-Thibaut CHASTELLIERE

-Florian FEUILLEPAIN

-Zinedine MAKHLOUF

-Hafsa LAACHIRI

#### Prerequisites :
vous devez installez :
```console
lxml
```
#### Installing :
Sous LINUX dans une fenetre de commande tapez :
````console
$ sudo apt-get install python3-lxml
````
#### How to use :
Pour lancer le programme il suffit de mettre le dossier Papers et le fichier gl.py dans un même dossier,puis d'ouvrir le terminal à partir de ce dossier et de lancer le programme avec Papers en argument .

Tapez la commande suivante dans le console pour effectuer la conversion :

    ```console

    $ python3 gl.py Papers -t     \\ pdf to text

    $ python3 gl.py Papers -x     \\ pdf to xml

    ```
   
Les pdf traités se retrouve dans le dossier Papers/result.

Dans chaque pdf traité on a identifié 3 choses : 
  -Le nom du fichier d’origine (dans une ligne)
  -Le titre du papier (dans une ligne)
  -Le résumé ou abstract de l’auteur (dans une ligne)
  -La bibliographie 
  -La conclusion
  -La discussion


