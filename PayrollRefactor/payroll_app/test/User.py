

class User:
    employee_id = None
    employee_name = None
    employee_last_name = None
    email = None
    password = None
    users = []


    def __init__(self, employee_id, employee_name, employee_last_name, email, password):
        self._employee_id = employee_id
        self._employee_name = employee_name
        self._employee_last_name = employee_last_name
        self._email = email
        self._password = password

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        self._employee_name = employee_name

    @property
    def employee_last_name(self):
        return self._employee_last_name

    @employee_last_name.setter
    def employee_last_name(self, employee_last_name):
        self._employee_last_name = employee_last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def create_user(self):
        self._employee_id = input("Insert employee ID: ")
        self._employee_name = input("Insert employee name: ")
        self._employee_last_name = input("Insert employee last name: ")
        self._email = input("Insert employee email: ")
        self._password = input("Insert password: ")

        user = {"id": self._employee_id, "name": self._employee_name, "last_name": self.employee_last_name,"email": self._email, "password": self._password}
        return user

    def show_users_data(self):
        for i in self.users:
            print(i)
            print("\n")
