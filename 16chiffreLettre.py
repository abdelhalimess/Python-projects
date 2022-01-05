import math

n = int(input("Saisir un nombre : "))
 
chiffres = int(math.log10(n))
 
num = 0
 
# Stocker l'inverse de n dans num */
while (n != 0):
    num = (num * 10) + (n % 10)
    n //= 10
 
# Trouver le nombre des zéros à la fin */
chiffres = chiffres - int(math.log10(num))
 
#
# Extraire le dernier chiffre du nombre et imprimer le nombre correspondant en
# mots jusqu'à ce que le nombre devienne 0
while (num != 0):
    v = num % 10
    if v == 0:
        print("Zéro")
    elif v == 1:
        print("Un")
    elif v == 2:
        print("Deux")
    elif v == 3:
        print("Trois")
    elif v == 4:
        print("Quatre")
    elif v == 5:
        print("Cinq")
    elif v == 6:
        print("Six")
    elif v == 7:
        print("Sept")
    elif v == 8:
        print("Huit")
    elif v == 9:
        print("Neuf")
 
    num //= 10
 
# afficher les zeros réstantes */
while (chiffres > 0):
    print("Zero ")
    chiffres -= 1