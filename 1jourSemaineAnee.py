num_of_days = int(input("Entrer le nombre de jours : "))
num_of_years = num_of_days // 365
num_of_weeks = (num_of_days % 365) // 7
num_of_days = (num_of_days % 365) % 7
print("Resultats:" ,num_of_years,"an(s),",num_of_weeks,"semaines et",num_of_days,"jours.")