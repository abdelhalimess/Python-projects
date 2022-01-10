import math
base = float(input("Enter the base : "))
exposant = float(input("Enter the exposant : "))
power = math.pow(base, exposant)
print('{0} ^ {1} = {2}'.format(base, exposant, power))
