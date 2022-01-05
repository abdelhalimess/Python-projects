num_1 = int(input("Entrer le premier nombre: "))
num_2 = int(input("Entrer le deuxieme nombre: ")) 
num_3 = int(input("Entrer le troisieme nombre: "))
max = int
if num_1 <= num_2:
    max = num_2 

elif num_1 >= num_2:
    max = num_1

    if max <= num_3:
        max = num_3
    
print("Le max = ",max)

