num_1 = int(input("Enter the first nombre: "))
num_2 = int(input("Enter the second nombre: ")) 
num_3 = int(input("Enter the third nombre: "))
max = int
if num_1 <= num_2:
    max = num_2 

elif num_1 >= num_2:
    max = num_1

    if max <= num_3:
        max = num_3
    
print("Le max = ",max)

