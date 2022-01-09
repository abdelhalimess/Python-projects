# Taille de la matrice
M = int(input("Entrer le nombre des lignes(colonnes): "))
N = M   # Matrice triangulaire supérieure est une matrice carrée
 
# Intialiser la taille du matrice
A = [[0 for i in range(N)] for j in range(M)]
 
# Entrer les éléments de A
for i in range(M):
    for j in range(N):
        A[i][j] = int(input("Entrer l'élement A[{0}][{1}] : ".format(i, j)))
 
# On suppose que c'est une matrice triangulaire supérieure 
triangSup = True

for i in range(M):
    for j in range(i):
        if(A[i][j] != 0):
            triangSup = False
            break
        
# Affichage de la matrice
print("La matrice = ")
for i in range(N):
    for j in range(M):
        print("    ",A[i][j],end="")
    print()

if(triangSup == True):
    print("\nCette matrice est triangulaire supérieure.\n")
else:
    print("\nCette matrice n'est pas triangulaire supérieure.\n")