
employee = {"name":"","last_name":"","position":"","raw_salary":0,"health_discount":0,"pension_discount":0,"final_salary":0}
employees = []
slmv = 1300000
rate_health_discount = 0.04
rate_pension_discount = 0.04
aux_money = 160200.0

# Start function
def start():
    option = 0
    
    while (option != 3):
        option = int(input("""
Welcome...
Select your option: 
1. Register
2. Login
3. Salir

 """))
        if(option == 1):
            register(rate_health_discount,rate_pension_discount,aux_money)
        else:
            login()

    print("\nBye")

# Calculate salary
def f_calculate_net_salary(salary,rate_health_discount,rate_pension_discount,aux_money):
    net_salary = salary - f_health_discount(salary,rate_health_discount) - f_pension_discount(salary,rate_pension_discount) + f_transport_aux(salary,aux_money)
    return net_salary

# Calculate pension discount
def f_health_discount(salary,rate_health_discount):
    return salary * rate_health_discount


# Calculate health discount
def f_pension_discount(salary,rate_pension_discount):
    return salary * rate_pension_discount

# Calculate transport aux
def f_transport_aux(salary,aux_money):
    if(salary >= (2 * slmv)):
        return 0
    else:
        return aux_money

# Register function
def register(rate_health_discount,rate_pension_discount,aux_money):
    name = input("Insert employee name: ")
    last_name = input("Insert employee last name: ")
    position = input("Insert employee position: ")
    raw_salary = float(input("Insert employee salary: "))
    health_discount = f_health_discount(raw_salary,rate_health_discount)
    pension_discount = f_pension_discount(raw_salary,rate_pension_discount)
    final_salary = f_calculate_net_salary(raw_salary,rate_health_discount,rate_pension_discount,aux_money)

    employee = {"name":name,"last_name":last_name,"position":position,"raw_salary":raw_salary,"health_discount":health_discount,"pension_discount":pension_discount,"final_salary":final_salary}
    employees.append(employee)
    

start()