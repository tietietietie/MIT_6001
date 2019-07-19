annual_salary=float(input("Enter your annual salary:"))
monthly_salary=annual_salary/12
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
monthly_saved=monthly_salary*portion_saved
total_cost=float(input("Enter the cost of your dream home:"))
portion_down_payment=0.25
down_payment=total_cost*portion_down_payment
r=0.04
Number_of_months=0
current_saving=0
while(current_saving<down_payment):
    current_saving=monthly_saved+current_saving*(1+r/12)
    Number_of_months+=1
print("Number of months:"+str(Number_of_months))