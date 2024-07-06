class Category:
    id = None
    name_category = None

    def __init__(self, id, name_category):
        self._id = id
        self._name_category = name_category

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name_category(self):
        return self._name_category

    @name_category.setter
    def name_category(self,name_category):
        self._name_category = name_category

    def create_category(self):
        self._id = input("Insert ID: ")
        self._name_category = input("Insert category name: ")

    