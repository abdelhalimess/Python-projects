#La taille de matrice 
n=int(input ("Entrer le nombre de colones(lignes): "))
m= n
# Intialiser la taille des matrices
A= [[0 for i in range(n)] for j in range(m)]
X=[0]*m
B=[0]*m
# Entrer les elements de la matrice A
for i in range(m):
    for j in range(n):
        A[i][j] = int(input("Entrer l'element A[{0}][{1}] : ".format(i, j)))

# Affichage de la matrice A
print("La matrice A =")
for i in range (m) :
    for j in range(n):
        print("   ",A[i][j], end="")
    print()
# Entrer les element de vecteur B 
for i in range(m):
    B[i]=int(input("Entrer l'element {0} : ".format(i+1)))
for i in range(m):
    print(B[i],'\n ')

# ----------- Triangularisation --------------
for k in range(1,n) :
   for i in range(k+1,n):
       w=A[i][k]/A[k][k]
       for j in range (1,n):
           
              A[i][j]=A[i][j]-w*A[k][j]  
       B[i]=B[i]-w*B[k]

# Affichage de la matrice A
print("La matrice A =")       
for i in range (m) :
    for j in range(n):
        print("   ",A[i][j], end="")
    print()
# Affichage de le vecteur B
print("Le vecteur B =")     
for i in range(m):
    print("  ",B[i],'\n ')

# --------------- Resolution ----------------

# Calcul du vecteur X
for i in range (m-1,-1,-1) :
      s=0
      for j in range (i+1,m) :
          s=s+A[i][j]*X[j]
      X[i]=(B[i]-s) / A [i][i]

# Affichage du vecteur X
print("La vecteur X =")        
for i in range(m):
    print("  ",X[i],'\n ')