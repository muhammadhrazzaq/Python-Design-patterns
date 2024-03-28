# Define the Burger class
class Burger:
    def __init__(self, patty, bun, veggies, sauce):
        self.patty = patty
        self.bun = bun
        self.veggies = veggies
        self.sauce = sauce

    def __str__(self):
        return f"{self.patty} burger with {self.bun}, {self.veggies}, and {self.sauce}"

# Define the BurgerBuilder class
class BurgerBuilder:
    def __init__(self):
        self.patty = None
        self.bun = None
        self.veggies = None
        self.sauce = None

    def add_patty(self, patty):
        self.patty = patty
        return self

    def add_bun(self, bun):
        self.bun = bun
        return self

    def add_veggies(self, veggies):
        self.veggies = veggies
        return self

    def add_sauce(self, sauce):
        self.sauce = sauce
        return self

    def build(self):
        return Burger(self.patty, self.bun, self.veggies, self.sauce)

# Use the BurgerBuilder
veggie_burger_builder = BurgerBuilder()
veggie_burger = veggie_burger_builder.add_patty("Veggie patty") \
                                     .add_bun("Sesame seed bun") \
                                     .add_veggies("Lettuce, tomato, onion") \
                                     .add_sauce("Vegan mayo") \
                                     .build()

chicken_burger_builder = BurgerBuilder()
chicken_burger = chicken_burger_builder.add_patty("Chicken patty") \
                                       .add_bun("Brioche bun") \
                                       .add_veggies("Lettuce, tomato, pickles") \
                                       .add_sauce("Mayo") \
                                       .build()

beef_burger_builder = BurgerBuilder()
beef_burger = beef_burger_builder.add_patty("Beef patty") \
                                 .add_bun("Sesame seed bun") \
                                 .add_veggies("Lettuce, tomato, onion") \
                                 .add_sauce("Ketchup, mustard") \
                                 .build()

print(veggie_burger)  # Output: Veggie patty burger with Sesame seed bun, Lettuce, tomato, onion, and Vegan mayo
print(chicken_burger)  # Output: Chicken patty burger with Brioche bun, Lettuce, tomato, pickles, and Mayo
print(beef_burger)  # Output: Beef patty burger with Sesame seed bun, Lettuce, tomato, onion, and Ketchup, mustard