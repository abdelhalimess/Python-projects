matière_1 = float(input('Enter the 1st mark : '))
matière_2 = float(input('Enter the 2nd mark : '))
matière_3 = float(input('Enter the 3rd mark : '))
matière_4 = float(input('Enter the 4th mark : '))
matière_5 = float(input('Enter the 5th mark : '))
total = matière_1 + matière_2 + matière_3 + matière_4 + matière_5
moyenne = total / 5.0
pourcentage = (moyenne * 100) / 20
print("Total = ", total)
print("Average = ", moyenne)
print("Percentage = ", pourcentage,"%")
