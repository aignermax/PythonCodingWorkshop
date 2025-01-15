class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        # Überschreiben der Methode
        print("Woof!")

if __name__ == "__main__":
    generic_animal = Animal("Generic")
    dog = Dog("Bello")

    generic_animal.make_sound()  # Ausgabe: Some generic animal sound.
    dog.make_sound()             # Ausgabe: Woof!
