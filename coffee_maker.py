class CoffeeMaker:


    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        print("Water: " + str(self.resources["water"]) + "ml")
        print("Milk: " + str(self.resources["milk"]) + "ml")
        print("Coffee: " + str(self.resources["coffee"]) + "g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print("Sorry there is not enough " + item + ".")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] = self.resources[item] - order.ingredients[item]
        print("Here is your " + order.name + ". Enjoy!")