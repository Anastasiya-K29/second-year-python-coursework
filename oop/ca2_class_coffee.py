#!/usr/bin/env python3

import ast
data = ast.literal_eval(input())

class Coffee:
    def __init__(self, price, type, size):
        self.price = price
        self.type = type
        self.size = size

    def __str__(self):
        return f"Type: {self.type}, Size: {self.size}, Price: {self.price}"


class Order:
    def __init__(self, id):
        self.id = id
        self.coffees = []

    def add_coffee(self, coffee_obj):
        self.coffees.append(coffee_obj)


class Bill:
    def __init__(self, order):
        self.order = order

    def get_total(self):
        total = 0
        for coffee in self.order.coffees:
            total += coffee.price
        return total

    def count_coffees(self):
        count = 0
        for coffee in self.order.coffees:
            count += 1
        return count

    def most_expensive(self):
        most = self.order.coffees[0]
        for coffee in self.order.coffees[1:]:
            if coffee.price > most.price:
                most = coffee
        return most

    def cheapest(self):
        least = self.order.coffees[0]
        for coffee in self.order.coffees[1:]:
            if coffee.price < least.price:
                least = coffee
        return least

    def count(self, coffee_type):
        count = 0
        for coffee in self.order.coffees:
            if coffee.type == coffee_type:
                count += 1
        return count

    def go_dutch(self):
        return self.get_total() / self.count_coffees()


order = Order(data["order_id"])

for item in data["items"]:
    coffee = Coffee(item["price"], item["type"], item["size"])
    order.add_coffee(coffee)

final_bill = Bill(order)

c1 = final_bill.most_expensive()
print(c1)
c2 = final_bill.cheapest()
print(c2)
print(final_bill.count("Irish"))
print(final_bill.get_total())
print(final_bill.go_dutch())