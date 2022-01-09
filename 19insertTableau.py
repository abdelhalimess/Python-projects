# Entrer la taille du tableau
N = int(input("Entrer le nombre d'éléments : "))

# Initialiser la taille du tableau
tab=[0]*(N+1)
 
# Entrer les éléments du tableau
for i in range(N):
    tab[i]= int(input("Entrer l'élement {0} : ".format(i+1)))

# Afficher le tableau avant l'insertion
print("Tableau avant insertion: ",end='  ')
for i in range(0,N):
     print(tab[i] , end="  |  ")

# Entrer l'élément et sa position d'insertion
num = int(input("\n\nEntrer un élément à ajouter : "))
pos = int(input("Entrer sa position :  "))
 
# Si la position n'est pas valide 
if (pos > N or pos <= 0):
    print("Position invalide! Veuillez entrer une position entre 1 et" , N)
else:
    # Faites de la place pour un nouvel élément de tableau
    # Décalage à droite juste après la position
    for i in range(N,pos-1,-1):
        tab[i] = tab[i-1]

    tab[pos - 1] = num    # Insertion du nouveau élément
    N += 1           # Incrémentation de la taille de tableau

        # ------- Affichage du tableau après l'opération d'insertion -------
    print("Tableau apés insertion: ",end="  ")
    for i in range(0,N):
        print(tab[i] , end="  |  ")