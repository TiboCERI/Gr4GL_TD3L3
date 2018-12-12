# Gr4GL_TD3L3

Le C++ est plus rapide que le python pour exécuter le même code de test.
Mais nous partons tout de même sur le python car il minimise les risques de bug et nous simplifie la partie développement.

### ******* version 2.0.0 *******
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

