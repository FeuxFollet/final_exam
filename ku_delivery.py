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
        order.status = "delivered"


class DeliveryOrder():
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = status
        self.driver = "None"

    def assign_driver(self, driver):
        self.driver = driver.name

    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}"

all_orders = []

customer1 = Customer("Alice", "32nd Good Wood Road")
customer2 = Customer("Bob", "Yellow Street")
driver1 = Driver("David", "Motorcycle")
customer1.introduce()
customer2.introduce()
driver1.introduce()
print()

order1 = customer1.place_order("Laptop")
order1.assign_driver(driver1)
all_orders.append(order1)
print(order1.summary())
print()

order2 = customer2.place_order("Headphones")
order2.assign_driver(driver1)
all_orders.append(order2)
print(order2.summary())
print()

driver1.deliver(order1)
driver1.deliver(order2)

print
print("Final Status:")
for i in all_orders:
    print(f"Order for {i.item} → {i.status}")

