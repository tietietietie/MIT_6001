annual_salary=float(input("Enter the starting salary:"))
total_cost=1000000
portion_down_payment=0.25
down_payment=total_cost*portion_down_payment
semi_annual_raise=0.07
r=0.04
Total_months=36
low=0
high=10000
mid=0
epsilon=100
num_guess=0
current_saving=0
while abs(current_saving-down_payment)>100 and low!=high:
    current_saving=0
    annual_salary_a=annual_salary #Reset the varibles
    mid=round((high+low)/2)
    portion_saved=mid/10000
    for Number_of_months in range(1,37):
        monthly_salary=annual_salary_a/12
        monthly_saved=monthly_salary*portion_saved
        current_saving=monthly_saved+current_saving*(1+r/12)
        if(Number_of_months%6==0):
            annual_salary_a=annual_salary_a*(1+semi_annual_raise)
    if(current_saving>=down_payment):
        high=mid
    else:
        low=mid
    num_guess += 1
if mid==10000 :
    print("It is not possible to pay the down in three years")
else:
    print("Best saving rate:"+str(portion_saved))
    print("Steps in bisection search:"+str(num_guess))
