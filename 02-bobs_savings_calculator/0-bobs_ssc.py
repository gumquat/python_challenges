#Greet Bob, then calculate his annual savings using the following income information:
#hourly_wage, hours_per_week, spend_per_week
greeting = "Hello "
name = "Bob"

hourly_wage = 20
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
workweeks_per_year = 48
income_per_year = workweeks_per_year * income_per_week #calc yearly income
spend_per_week = 400
spend_per_year = spend_per_week * 52 #calc yearly spendature

print(greeting + name) #greeting
print(name + ", your yearly income is: {:d}".format(income_per_year)) #print yearly income
print(name + ", your yearly spendature is: {:d}".format(spend_per_year)) #print yearly spendature
print(name + ", your yearly savings comes to a total of {:d}".format(income_per_year - spend_per_year))