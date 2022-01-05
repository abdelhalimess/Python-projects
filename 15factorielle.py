num = int(input("Entrer le nombre: "))
fact = 1
if(num >= 0):  
    for i in range(1,num+1):
        fact = fact * i  
    print("{0}!  =  {1}".format(num,fact))     
else:
    print("\n        ERREUR!\n")
       