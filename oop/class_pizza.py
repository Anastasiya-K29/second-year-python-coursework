#!/usr/bin/env python3

import ast
input_list = ast.literal_eval(input())

class Pizza:
    def __init__(self, size, topping, price):
        self.size = size
        self.topping = topping
        self.price = price

    def __eq__(self, other):
        return self.price == other.price
    
    def __gt__(self, other):
        return self.size > other.size
    
    def __lt__(self, other):
        return self.size < other.size
    
class StandardPizza(Pizza):
    def __init__(self, topping, price):
        super().__init__(9, topping, price)

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.price
        return total

order = Order()

for item in input_list:
    if len(item) == 3:
        pizza = Pizza(item[0], item[1], item[2])
    else:
        pizza = Pizza(item[0], item[1])

    order.add_pizza(pizza)

print(order.get_total())
