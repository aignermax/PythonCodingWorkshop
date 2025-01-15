# lsp_refactored.py

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird, ABC):
    @abstractmethod
    def fly(self):
        pass

class Eagle(FlyingBird):
    def make_sound(self):
        print("Screech!")

    def fly(self):
        print("Eagle is flying")

class Ostrich(Bird):
    def make_sound(self):
        print("Boo-boo!")

    # Ostrich does NOT have a fly() method, because it doesn't fly.
    # We separated birds that can fly (FlyingBird) from those that cannot.
