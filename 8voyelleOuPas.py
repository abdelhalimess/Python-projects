char = input("Enter letter: ")
if str.lower(char) in ('aeiouy'):
    print("\nCet alphabet est une voyelle.\n")
elif str.lower(char) in ('bcdfghjklmnpqrstvwxz'):
    print("\nCet alphabet est une consonne.\n")    
else:
    print("\n Erreur !\n")