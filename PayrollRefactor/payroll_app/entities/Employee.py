from payroll_app.entities.User import User


class Employee(User):

    salary = None
    rol = None

    # Constructor
    def __init__(self, employee_id,employee_name, employee_last_name, email, password, rol, salary):
        super().__init__(employee_id,employee_name, employee_last_name, email, password)
        self._rol = rol
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        self._salary = salary

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self,rol):
        self._rol = rol

    def create_employee(self):
        super().create()
        self._rol = input("Insert rol: ")
        self._salary = float(input("Insert raw salary: "))

        employee_saved = {}

        employee_saved[self._id] = {"name": self._name, "last_name": self._last_name, "email": self._email, "password": self._password, "rol": self._rol, "salary": self._salary}
        self.save(employee_saved)
