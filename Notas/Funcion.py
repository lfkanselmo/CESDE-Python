# def for functions

salary = float(input("Insert the salary: "))
slmv = float(input("Insert minimum salary: "))
rate_health_discount = 0.04
rate_pension_discount = 0.04
aux_money = 160200.0

# Calculate pension discount
def health_discount(salary,rate_health_discount):
    return salary * rate_health_discount


# Calculate health discount
def pension_discount(salary,rate_pension_discount):
    return salary * rate_pension_discount

# Calculate transport aux
def transport_aux(salary,aux_money):
    if(salary >= (2 * slmv)):
        return 0
    else:
        return aux_money

# Calculate salary
def calculate_net_salary(salary,rate_health_discount,rate_pension_discount,aux_money):
    net_salary = salary - health_discount(salary,rate_health_discount) - pension_discount(salary,rate_pension_discount) + transport_aux(salary,aux_money)
    return net_salary

finalSalary = calculate_net_salary(salary,rate_health_discount,rate_pension_discount,aux_money)
print(f"Your salary is: {finalSalary}")