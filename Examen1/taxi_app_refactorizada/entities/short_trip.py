from entities.service import service
class short_trip(service):
    def __init__(self, base_fee=10):
        super().__init__("Short Trip", base_fee)