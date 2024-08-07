class category:
    id = None
    name_category = None
    _categories = {}

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

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories

    def create_category(self):
        self._id = input("Insert category ID: ")
        self._name_category = input("Insert category name: ")
        self.categories[self._id] = {"Id": self._id, "Name": self._name_category}

    @classmethod
    def search_category(cls):
        founded = False
        category_founded = None


        while not(founded):
            cat = input("Insert your category to search: ")
            for item in category._categories.values():
                if item["Name"] == cat:
                    founded = True
                    print(f"Category {cat} correctly assigned")
                    return item
            print(f"Category {cat} not found... try again")
        return category_founded