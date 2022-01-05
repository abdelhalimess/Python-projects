import math
base = float(input("Entrer la base : "))
exposant = float(input("Entrer l'exposant : "))
power = math.pow(base, exposant)
print('{0} ^ {1} = {2}'.format(base, exposant, power))
