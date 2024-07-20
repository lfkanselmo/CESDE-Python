from domain.user import user


class employee(user):

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

    def create(self):
        super().create()
        self._rol = input("Insert rol: ")
        self._salary = int(input("Insert salary: "))