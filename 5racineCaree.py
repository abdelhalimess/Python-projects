import math
num = float(input("Entrer un nombre : "))

if num >= 0 :
    square_root = math.sqrt(num) 
    print("La racine caree de {0} = {1}".format(num,square_root))
else: print("   ERREUR !") 