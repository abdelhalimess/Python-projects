num = input("Entrer le nombre: ")
for i in range(0,len(num)):
    if (num[i] == "0"): 
        print("Zero",end=' ')

    elif (num[i] == "1"): 
        print("Un",end=' ')
            
    elif (num[i] == "2"): 
        print("Deux",end=' ')

    elif (num[i] == "3"): 
        print("Trois",end=' ')

    elif (num[i] == "4"): 
        print("Quatre",end=' ')

    elif (num[i] == "5"): 
        print("Cinq",end=' ')

    elif (num[i] == "6"): 
       print("Six",end=' ')

    elif (num[i] == "7"): 
        print("Sept",end=' ')

    elif (num[i] == "8"): 
        print("Huit",end=' ')

    elif (num[i] == "9"): 
        print("Neuf",end=' ')

    elif (num[i] not in ("0123456789")):
        print(num[i],end='  ')    






        