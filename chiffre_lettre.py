d1 = {"Nom":"Esselami","Prenom":'Abdelhalim',"Age":19,"Taille":1.75,"Poids":'60kg'}

def f(d):
    for k,v in d.items():
        print( k ,'=', v )
    print('d1 = ',d)

f(d1)