# Taille de la matrice
M = int(input("Entrer le nombre des lignes: "))
N = int(input("Entrer le nombre des colonnes: "))
 
# Initialiser la taille des matrices
A = [[0 for i in range(N)] for j in range(M)]
B = [[0 for i in range(M)] for j in range(N)]
 
# Entrer les éléments de A
for i in range(M):
    for j in range(N):
        A[i][j] = int(input("Entrer l'élement A[{0}][{1}] : ".format(i, j)))

# Affichage de la matrice
print("La matrice =")
for i in range(M):
    for j in range(N):
        print("   ",A[i][j], end="")
    print()

for i in range(N):
    for j in range(M):
        B[i][j] = A[j][i]
 
# Afficher la matrice transposée
print("Sa transposée =")
for i in range(N):
    for j in range(M):
        print("   ",B[i][j], end="")
    print()
    