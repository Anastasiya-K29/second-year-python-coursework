#!/usr/bin/env python3

import ast
order_data = ast.literal_eval(input())

class Burger:
    def __init__(self, name, base_price, is_vegan):
        self.name = name
        self.base_price = base_price
        self.toppings = []
        self.is_vegan = is_vegan

    def add_topping(self, topping_name, price_increase):
        self.toppings.append(topping_name)
        self.base_price += price_increase
        if topping_name == "Bacon" or topping_name == "Cheese":
            self.is_vegan = False

    def __str__(self):
        return f"Burger({self.name}, price={self.base_price})"


class ComboDeal:
    def __init__(self):
        self.burgers = []

    def add_burger(self, burger_obj):
        self.burgers.append(burger_obj)

    def apply_discount(self, percent):
        for burger in self.burgers:
            burger.base_price = burger.base_price - (burger.base_price * percent / 100)

    def get_vegan_options(self):
        vegan_names = []
        for burger in self.burgers:
            if burger.is_vegan == True:
                vegan_names.append(burger.name)
        return vegan_names


combo = ComboDeal()

for item in order_data:
    burger = Burger(item["name"], item["price"], item["vegan"])
    burger.add_topping(item["extra"][0], item["extra"][1])
    combo.add_burger(burger)

combo.apply_discount(10)
print(combo.get_vegan_options())