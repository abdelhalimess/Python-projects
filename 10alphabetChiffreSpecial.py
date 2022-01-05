char = str.lower(input("Entrer un caractère: "))

if char in ('abcdefghijklmnopqrstuvwxyz'):
    print("\n Cet caractère est un alphabet.\n")
elif char in ('0123456789'):
    print("\n Cet caractère est un chiffre.\n")
else: 
    print("\n Cet caractère est un caractère spécial.\n")        