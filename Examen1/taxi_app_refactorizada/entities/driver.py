class driver:
    name = None
    total_earnings = 0
    current_service = None
    vehicle = None
    def __init__(self, name, vehicle):
        self._name = name
        self._total_earnings = 0
        self._current_service = None
        self.vehicle = vehicle

    def assign_service(self, service):
        self._current_service = service

    def calculate_earnings(self):
        if self._current_service:
            self._total_earnings += self._current_service.calculate_fee()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def total_earnings(self):
        return self._total_earnings

    @total_earnings.setter
    def total_earnings(self,total_earnings):
        self._total_earnings = total_earnings

    @property
    def current_service(self):
        return self._current_service

    @current_service.setter
    def current_service(self, current_service):
        self._current_service = current_service
