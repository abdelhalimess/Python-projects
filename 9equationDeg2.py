import math
print("\n      *EQUATION DU 2EME DEGRE [Ax² + Bx + C = 0]*\n")
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
delta = math.pow(B,2) - 4*(A*C)
if delta < 0:
    print("\nIl n'y a pas de racine à cette equation.")
elif delta == 0:
    X = -B / (2*A)
    print("\n Il ya une seule racine = ",X)
elif delta > 0:
    X1 = ( -B + (math.sqrt(delta)) )/ (2*A)
    X2 = ( -B - (math.sqrt(delta)) )/ (2*A)
    print("Les deux racines de cette equation sont X1 = {0}, X2 = {1}.".format(X1,X2))          