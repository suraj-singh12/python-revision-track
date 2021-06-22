class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bhau Bhau")

tomi = Dog()
tomi.bark()