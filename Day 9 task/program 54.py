class Herbivore:
    def eat_plants(self):
        print("Herbivore eats plants.")
class Carnivore:
    def eat_meat(self):
        print("carnivore eats meat.")
class Omnivore:
    def eat_both(self):
        print("omnivore eats plants and meat both.")
class Bear(Herbivore,Carnivore,Omnivore):
 pass
bear = Bear()
bear.eat_plants()
bear.eat_meat()
bear.eat_both()            