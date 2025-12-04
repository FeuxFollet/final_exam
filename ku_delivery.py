class Person():
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f"Hi, I'm {self.name}.")


class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(self.name, item, "preparing")


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")


class DeliveryOrder():
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = status
        self.driver = "None"

    def assign_driver(self, driver):
        self.driver = driver

    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}"    
    