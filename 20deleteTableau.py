taille = int(input("Entrer le nombre d'éléments : "))
 
# Intialiser la taille des tableaux avec taille
tab=[0]*(taille)
 
# Entrer les éléments du tableau source
for i in range(taille):
    tab[i]=int(input("Entrer l'élement {0} : ".format(i+1)))

    #  Afficher le tableau avant suppression
print("Tableau avant supression:",end="  ") 
for i in range(taille):
    print(tab[i] , end="  |  ") 
 
pos = int(input("\nEntrer la position de l'élément à supprimer : "))
 
# Si la position n'est pas valide
if (pos > taille + 1 or pos <= 0):
    print("Position invalide! Veuillez entrer une position entre 1 et " , taille)
else:
    # Copier la valeur de l'élément suivant dans l'élément actuel
    for i in range(pos-1, taille-1):
        tab[i] = tab[i + 1]
 
    # Décrémenter taille du tableau
    taille-=1

    # ------- Afficher le tableau après suppression -------
    print("Tableau aprés supression:",end="  ") 
    for i in range(taille):
        print(tab[i] , end="  |  ")