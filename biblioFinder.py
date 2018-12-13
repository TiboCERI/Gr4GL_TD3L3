def biblioFinder(normalContent, lowerContent) :
	
	indexFound = lowerContent.find("\nreferences\n")
	if indexFound == -1 :
		return "bibliography not found"
	indexFound += len("\nreferences\n")
	normalContent = normalContent[indexFound:]
	indexFound = normalContent.find("\n\n");
	if indexFound == -1 :
		return "bibliography not found"
	normalContent = normalContent[:indexFound]
	return normalContent


fichier = open("test.txt", 'r')
contenu = fichier.read()
contenuLowerCase = contenu.lower()
fichier.close()
print(biblioFinder(contenu, contenuLowerCase))
