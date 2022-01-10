num_of_days = int(input("Enter the number of days: "))
num_of_years = num_of_days // 365
num_of_weeks = (num_of_days % 365) // 7
num_of_days = (num_of_days % 365) % 7

print("Results:" ,num_of_years,"year(s),",num_of_weeks,"week(s) and",num_of_days,"day(s).")