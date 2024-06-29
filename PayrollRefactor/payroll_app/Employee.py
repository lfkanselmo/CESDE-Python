from payroll_app.test.User import User


class Employee(User):

    employee_id = None
    employee_name = None
    employee_last_name = None
    email = None
    password = None
    salary = None
    rol = None

    # Constructor
    def __init__(self, employee_id,employee_name, employee_last_name, email, password, rol, salary):
        super().__init__(employee_id,employee_name, employee_last_name, email, password)
        self._rol = rol
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self,employee_id):
        self._employee_id = employee_id

    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self,employee_name):
        self._employee_name = employee_name

    @property
    def employee_last_name(self):
        return self._employee_last_name

    @employee_last_name.setter
    def employee_last_name(self,employee_last_name):
        self._employee_last_name = employee_last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password = password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self,rol):
        self._rol = rol

    def create_user(self):
        employee = super().create_user()
        self._rol = input("Insert rol: ")
        self._salary = float(input("Insert employee raw salary: "))

        employee = {"id": employee["id"], "name": employee["name"], "last_name": employee["last_name"],"email": employee["email"], "password": employee["password"], "rol":self._rol, "salary": self._salary}
        User.users.append(employee)
