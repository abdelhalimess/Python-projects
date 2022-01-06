liste =[17, 38, 10, 25, 72]
print("* La liste: ",liste)
liste.sort()
print("* La liste triée: ",liste)

liste.append(12)
print("* L'ajout d'element 12: ",liste)

liste.reverse()
print("* La liste renversée: ",liste)

for i in range(0,len(liste)):
    if liste[i] == 17:
        print("* Indice de 17 = ",i)

liste.remove(38)
print("* La suppression de 38: ",liste)

print("* La sous-liste du 2e au 3e élément: ",liste[1:3])

print("* La sous-liste du début au 2e élément ",liste[:2])

print("* La sous-liste du 3e élément à la fin de la liste: ",liste[2:])

print("* La sous-liste complète de la liste: ",liste[:])

print("* Le dernier élément: ",liste[-1])