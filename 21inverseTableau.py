# Entrer la taille du tableau
N = int(input("Entrer le nombre d'éléments : "))
 
# Initialiser la taille du tableau
tab=[0]*(N)
 
# Entrer les éléments du tableau
for i in range(N):
    tab[i]=int(input("Entrer l'élement {0} : ".format(i+1)))

# ------- Afficher le tableau avant inversion ------- 
print("Tableau avant inversion:",end="  ")
for i in range(N):
    print(tab[i] ,end= "  |  ")

indexArriere = 0
indexAvant = N - 1
while (indexArriere < indexAvant):
    # Inverser le dernier élément avec le premier élément
    temp = tab[indexArriere]
    tab[indexArriere] = tab[indexAvant]
    tab[indexAvant] = temp
 
    # Incrémenter l'index du premier élément et décrémenter l'index du dernier
    indexArriere+=1
    indexAvant-=1
 
# ------- Afficher le tableau après inversion ------- 
print("\nTableau aprés inversion:",end="  ")
for i in range(N):
    print(tab[i] ,end= "  |  ")