

class user:
    id = None
    name = None
    last_name = None
    email = None
    password = None
    users = []


    def __init__(self, id, name, last_name, email, password):
        self._id = id
        self._name =name
        self._last_name = last_name
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

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

    def create(self):
        self._id = input("Insert ID: ")
        self._name = input("Insert name: ")
        self._last_name = input("Insert last name: ")
        self._email = input("Insert email: ")
        self._password = input("Insert password: ")

    def show_data(self):
        for i in self.users:
            print(i)
            print("\n")


    def save(self,user_new):
        user.users.append(user_new)