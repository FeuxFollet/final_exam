# KU OOP Delivery Program

This is an OOP which simulates a simple delivery service where customers can place order and drivers can deliver them.

## Features

- You can create customers and driver objects.
- Cutomers can place an order of an item.
- The order will be created as an object and will initially be on "preparing".
- A driver can be assigned to each order and can also deliver them which will change the status from "preparing" to "delivered".

(Additional features)
- Added an OrderCentre class so the program fits the OOP theme more.

## Project Structure

- `ku_delivery.py`: Defines all the class nessecary for this program and also run the test at the same time.
- `README.md` : Contains all the information about the program.

## Person Class

A parent class that stores the common attribute and method for Customer and Driver class.

### Attributes
- `name` (str): The person's name.

### Methods
- `introduce()`: Introduce the person by printing out the name.

## Customer Class

A child class from the Person class, represents a customer

### Attributes
- `name` (str): The customer's name.
- `address` (str) : The cusomter's address.

### Methods
- `place_order(item)` : Creates an order object for the item.

## Driver Class

A child class from the Person class, represents a driver.

### Attributes
- `name` (str): The driver's name.
- `vehicle` (str) : The driver's vehicle.

### Methods
- `deliver(order)`: Delivers the order and change the order status from "preparing" to "delivered".

## DeliveryOrder Class

Represents an order made by the customer.

### Attributes
- `customer` (str): Name of the customer who made this order.
- `item` (str) : Name of the item the customer wants to order.
- `status` (str) : Status of the order.
- `driver` (str) : Name of the driver who will deliver the order. (Initially none if nobody is assigned to this order)

### Methods
- `assign_driver(driver)`: Assign a driver to the order.
- `summary()` : Returns the summary text for the order.

## OrderCentre Class

A class to store all orders and to get the final status. Added to make the program fit the OOP theme more.

### Attributes
- `all_order` (list): List that stores all orders.

### Methods
- `final_status()` : Prints out the final status for all orders.

## Project Status

The project is 100% implemented based on the required features with no errors, also containing an extra class to make the program fit the OOP theme more

##  Running the Program

To run the simulation, execute `ku_delivery.py`:

```bash
python ku_delivery.py
