from entities.driver import driver
from entities.vehicle import vehicle
from entities.long_trip import long_trip
from entities.short_trip import short_trip

vehicle = vehicle("Toyota", "Camry", 2020)
driver = driver("John", vehicle)
short_trip_service = short_trip()
long_trip_service = long_trip()

# Asignar y calcular ganancias para un viaje corto
driver.assign_service(short_trip_service)
driver.calculate_earnings()
print(f"{driver.name}'s total earnings after a short trip: {driver.total_earnings}")

# Asignar y calcular ganancias para otro viaje corto
driver.assign_service(short_trip_service)
driver.calculate_earnings()
print(f"{driver.name}'s total earnings after a short trip: {driver.total_earnings}")


# Asignar y calcular ganancias para un viaje largo
driver.assign_service(long_trip_service)
driver.calculate_earnings()
print(f"{driver.name}'s total earnings after a long trip: {driver.total_earnings}")

# Mostrar datos y vehiculo del conductor
print(driver.vehicle.__str__())