from random import *


class Person:
    def __init__(self, first_name, last_name, email, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone


class Customer(Person):

    def __init__(self, first_name, last_name, email, address, phone, order_id, user_id):
        super().__init__(first_name, last_name, email, address, phone)
        self.order_id = order_id
        self.user_id = user_id

    def get_order_id(self):
        return self.order_id


class Employee(Person):
    def __init__(self, first_name, last_name, email, address, phone, employee_id, employee_position, employee_salary):
        super().__init__(first_name, last_name, email, address, phone)
        self.employee_id = employee_id
        self.employee_position = employee_position
        self.employee_salary = employee_salary

    def get_employee_id(self):
        return self.employee_id

    def get_position(self):
        return self.employee_position

    def get_salary(self):
        return self.employee_salary


class Guest(Person):
    def __init__(self, first_name, last_name, email, address, phone, guest_id, guest_order_id):
        super().__init__(first_name, last_name, email, address, phone)
        self.guest_id = guest_id
        self.guest_order_id = guest_order_id

    def get_guest_id(self):
        return self.guest_id

    def get_order_id(self):
        return self.guest_order_id


class Pizza:

    def __init__(self, pizza_type, size, crust, sauce):
        self.pizza_type = pizza_type
        self.size = size
        self.crust = crust
        self.sauce = sauce

    def get_pizza_type(self):
        return self.pizza_type

    def get_size(self):
        return self.size

    def get_sauce(self):
        return self.sauce


class Cheesesteak(Pizza):
    def __init__(self, pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = ['cheesesteak', 'onions']

    def get_toppings(self):
        return self.toppings


class Cheese(Pizza):
    def __init__(self, pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = "cheese"

    def get_toppings(self):
        return self.toppings


class Pepperoni(Pizza):
    def __init__(self,pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = 'pepperoni'

    def get_toppings(self):
        return self.toppings


class Meatlovers(Pizza):
    def __init__(self, pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = ['pepperoni', 'sausage', 'bacon']

    def get_toppings(self):
        return self.toppings


class Veggies(Pizza):
    def __init__(self, pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = ['basil', 'onions', 'bell', 'pepper', 'olives']

    def get_toppings(self):
        return self.toppings


class Margarita(Pizza):
    def __init__(self, pizza_type, size, crust, sauce, toppings):
        super().__init__(pizza_type, size, crust, sauce)
        self.toppings = ['tomato','basil']

    def get_toppings(self):
        return self.toppings


class Order:
    def __init__(self, order_items, order_bill, order_id):
        self.order_items = order_items
        self.order_bill = order_bill
        self.order_id = order_id

    def get_order_items(self):
        return self.order_items

    def get_order_bill(self):
        return self.order_bill

    def get_order_id(self):
        return self. order_id


class CreditCard:
    def __init__(self, number, address, cvc, expiration):
        self.number = number
        self.address = address
        self.cvc = cvc
        self.expiration = expiration

    def get_number(self):
        return self.number

    def get_address(self):
        return self.address

    def get_cvc(self):
        return self.cvc

    def get_expiration(self):
        return self.expiration

    def last_four(self):
        last_four_numbers = self.number[-4:]  # gets the last 4 digits
        return last_four_numbers


def welcome_message():
    print("    *********************************")
    print("    *                               *")
    print("    *  Welcome to Angelo's Pizzaria *")
    print("    *                               *")
    print("    *********************************")


def pickup_or_delivery():
    print()
    valid_answer = ['p', 'd']
    option = input("Would you like your order to be pick-up or delivery?(p/d): ")
    option_lower = option.lower()
    while option_lower not in valid_answer:
        print("Your response is invalid. Please choose p for pick up or d for delivery.")
        option = input("Would you like your order to be pick-up or delivery?(p/d): ")
        option_lower = option.lower()
    if option_lower == 'd':
        print("You have decided that your order will be delivery.")
    else:
        print("You have decided that your order will be pick-up.")




def options():
    print()
    menu = ["cheesesteak","cheese","pepperoni","meatlovers","veggies","margarita"]
    total_items = []
    price = " "
    print("Here are the topping options: {}".format(menu))
    items = input("Please a topping: ")
    for pizza in items:
        if pizza == 'cheesesteak':
            return Cheesesteak()
        elif pizza == 'cheese':
            return Cheese()
        elif pizza == 'pepperoni':
             return Pepperoni()
        elif pizza == 'meatlovers':
            return Meatlovers()
        elif pizza == 'veggies':
            return Veggies()
        elif pizza == 'margarita':
            return Margarita()
    total_items.append(items)

def cash_or_cc():
    print()
    valid_cash_cc = ["cash", "cc"]
    cash_or_cc = input("How would you like to pay? Cash or Credit Card?(cash/cc): ")
    lower_cass_cc = cash_or_cc.lower()
    while lower_cass_cc not in valid_cash_cc:
        print()
        print("That's not a valid input. Please put either 'cash' for cash, or 'cc' for credit card.")
        cash_or_cc = input("How would you like to pay? Cash or Credit Card?(cash/cc): ")
        lower_cass_cc = cash_or_cc.lower()
    return cash_or_cc


def pay_cc():
    print()
    get_cc_name = input("Name on the card: ")
    get_cc_number = input("Credit Card Number: ")
    get_cc_address = input("Address for that card: ")
    get_cc_cvc = input("CVC number on the card: ")
    get_cc_expire = input("The expiration for that card: ")
    return get_cc_number, get_cc_address, get_cc_expire, get_cc_name


def main():
    welcome_message()
    pickup_or_delivery()
    order = options()
    price1 = 8.99
    price2 = 11.99
    order_items = order
    order_bill = order
    order_id = randint(100, 1000)
    order1 = Order(order_items, order_bill, order_id)



    if order_items == 'cheese' or 'pepperoni' or 'veggies':
        print("Your total amount is ${}".format(price1))

    elif order_items == 'cheeseteak' or 'meatlovers' or 'margarita':
        print("Your total amount is ${}".format(price2))

    payment_method = cash_or_cc()
    if payment_method == "cash":
        print("You've chosen to pay cash.")
    else:
        credit_card_payment = pay_cc()
        make_cc_payment = CreditCard(credit_card_payment[0], credit_card_payment[1], credit_card_payment[2],credit_card_payment[3])
        print("We've charged the card ending in {} the amount ${:.2f}!".format(make_cc_payment.last_four(),
                                                                               order1.get_order_bill()))
    print("Than you for your order!")
    print("Your order number is {}.".format(order1.get_order_id()))

main()



