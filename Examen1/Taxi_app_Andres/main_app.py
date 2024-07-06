# structured_version.py


# Taxi Application - Structured Programming Version with Driver and Vehicle Classes

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


# Function to assign a service to a driver
def assign_service(driver, service):
    # Assign the service to the driver
    driver.service = service


# Function to calculate the earnings for a taxi driver
def calculate_earnings(driver):
    # Get the service assigned to the driver
    service = driver.service

    # Calculate the earnings based on the service
    if service == "Short Trip":
        earnings = 10
    elif service == "Long Trip":
        earnings = 20
    else:
        earnings = 0

    # Add the earnings to the driver's total earnings
    driver.add_earnings(earnings)


# Main function
def main():
    # Create a driver and a vehicle
    driver = Driver("John")
    vehicle = Vehicle("Toyota", "Camry", 2020)

    # Example of assigning a service and calculating earnings
    assign_service(driver, "Short Trip")
    calculate_earnings(driver)
    print(f"{driver.name}'s total earnings after a short trip: {driver.total_earnings}")

    assign_service(driver, "Long Trip")
    calculate_earnings(driver)
    print(f"{driver.name}'s total earnings after a long trip: {driver.total_earnings}")


# Check if this script is the main program and run it
if __name__ == "__main__":
    main()