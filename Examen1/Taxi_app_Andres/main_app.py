
class Driver:
    def __init__(self, name):
        self.name = name
        self.total_earnings = 0

    def add_earnings(self, amount):
        self.total_earnings += amount


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year



def assign_service(driver, service):
    # Assign the service to the driver
    driver.service = service



def calculate_earnings(driver):
    service = driver.service

    if service == "Short Trip":
        earnings = 10
    elif service == "Long Trip":
        earnings = 20
    else:
        earnings = 0

    driver.add_earnings(earnings)


def main():

    driver = Driver("John")
    vehicle = Vehicle("Toyota", "Camry", 2020)


    assign_service(driver, "Short Trip")
    calculate_earnings(driver)
    print(f"{driver.name}'s total earnings after a short trip: {driver.total_earnings}")

    assign_service(driver, "Long Trip")
    calculate_earnings(driver)
    print(f"{driver.name}'s total earnings after a long trip: {driver.total_earnings}")



if __name__ == "__main__":
    main()