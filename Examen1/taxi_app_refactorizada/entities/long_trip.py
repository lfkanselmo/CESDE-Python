from entities.service import service


class long_trip(service):
    def __init__(self, base_fee=20):
        super().__init__("Long Trip", base_fee)