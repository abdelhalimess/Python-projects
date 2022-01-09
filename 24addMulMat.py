# Taille de la matrice A
M = int(input("Entrer le nombre des lignes: "))
N = int(input("Entrer le nombre des colonnes: "))
 
# Intialiser la taille du matrice A
A = [[0 for i in range(N)] for j in range(M)]
 
# Entrer les éléments de A
for i in range(M):
    for j in range(N):
        A[i][j] = int(input("Entrer l'élement A[{0}][{1}] : ".format(i, j)))

# Afficher la matrice A 
print("La matrice A =")
for i in range(M):
    for j in range(N):
        print("   ",A[i][j], end="")
    print()

# Intialiser la taille du matrice B
m = int(input("Entrer le nombre des lignes: "))
n = int(input("Entrer le nombre des colonnes: "))
B = [[0 for i in range(n)] for j in range(m)]

# Entrer les éléments de B
for i in range(m):
    for j in range(n):
        B[i][j] = int(input("Entrer l'élement B[{0}][{1}] : ".format(i, j)))

# Afficher la matrice B
print("La matrice B =")
for i in range(m):
    for j in range(n):
        print("   ",B[i][j], end="")
    print()

# Initialiser la taille de la matrice C
C = [[0]*m for i in range(n)]

# Si elles sont de mêmes dimensions
if(M == m and N == n):
# Remplir la matrice C avec la somme des matrices A et B    
    for i in range(n):
        for j in range(m):
            C[i][j]= A[i][j] + B[i][j]

# Afficher la matrice C            
    print("La somme = ")
    for i in range(m):
        for j in range(n):
         print("   ",C[i][j], end="")
        print()
              
else:
    print("\nPour faire la somme de deux matrices il faut qu'elles sont de mêmes dimensions!\n")

# Initialiser la taille de la matrice D
D = [[0 for i in range(n)] for j in range(M)]

# Si le nombre de colonnes de la matrice A est égal au nombre de lignes de la matrice B
if(N == m):
    
# Remplir la matrice D avec le produit des deux matrice A et B        
    for i in range(M):
        for j in range(n):
            produit = 0         
            for k in range(N):    
                produit += A[i][k] * B[k][j]
            D[i][j] = produit
# Afficher la matrice D              
    print("La multiplication = ")
    for i in range(M):
        for j in range(n):
            print("   ",D[i][j], end="")
        print()
else:
    print("\nLa multiplication est possible si et seulement si le nombre de colonnes de la matrice A est égal au nombre de lignes de la matrice B.\n")