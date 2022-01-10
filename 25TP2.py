# Size of matrix 
N=int(input ("Enter the number of columns: "))
m=int(input("Enter the number of lines: "))
# Intialise dimensions
A= [[0 for i in range(N)] for j in range(m)]
X=[0]*m
B=[0]*m
# Enter the elements of A
for i in range(m):
    for j in range(N):
        A[i][j] = int(input("Enter element A[{0}][{1}] : ".format(i, j)))

# Display elements of the matrix A
print("Matrix A =")
for i in range (m) :
    for j in range(N):
        print("   ",A[i][j], end="")
    print()

#Enter the elements of array B 
for i in range(m):
    B[i]=int(input("Enter element {0} : ".format(i+1)))
for i in range(m):
    print(B[i],'\n ')

# ----------- Triangularisation --------------
for k in range(0,N) :
   for i in range(k+1,N):
       w=A[i][k]/A[k][k]
       for j in range (0,N):
           
              A[i][j]=A[i][j]-w*A[k][j]  
       B[i]=B[i]-w*B[k]

for i in range (m):
    for j in range(N):
        print("   ",A[i][j],end="")
    print("")
for i in range(m):
    print("  ",B[i],'\n ')         
# ----------------- Resolution -------------------

for i in range (m-1,-1,-1) :
      S=0
      for j in range (i+1,m) :
          S=S+A[i][j]*X[j]
      X[i]=(B[i]-S) / A [i][i]

# Display X
print("X = ")      
for i in range(m):
    print("  ",X[i],'\n ')

   