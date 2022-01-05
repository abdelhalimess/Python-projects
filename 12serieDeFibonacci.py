n = int(input("Entrer le nombre de termes : "))
A = 0
B = 1
C = 0
print("Termes de la serie de Fibonacci : ")

for i in range(1,  n+1):
    print(C, end='  ')
    A = B
    B = C 
    C = A + B