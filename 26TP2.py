import numpy as np 
n=int(input ("Entrer le nombre de lignes: "))
m=int(input("Entrer le nombre de colones: "))

# Intialiser la taille de la matrice A
A= ( [[0 for i in range(n)] for j in range(m)])
for i in range(m):
    for j in range(n):
        A[i][j] = int(input("Saisir l'élement A[{0}][{1}] : ".format(i, j)))

# Affichage de la matrice A
print("La matrice A =")
for i in range (m) :
    for j in range(n):
        print("   ",A[i][j], end="")
    print()
    
L = np.identity(n)
U = np.zeros(shape=(n,n))
for i in range(1, n-1):
   for j in range (i+1,n):
       L[j][i]=A[j][i]/A[i][i]
   for j in range (i,n):
        U[i][j]=A[i][j]
   for j in range (i+1,n):
        for k in range(i+1,n):
            A[j][k]=A[j][k]-L[j][i]*U[i][k]
U[-1][-1] = A[-1][-1]
print("U = ")    
print(U)
print("L = ") 
print(L)
