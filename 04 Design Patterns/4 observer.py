from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def detach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer: 'Observer'):
        self._observers.append(observer)

    def detach(self, observer: 'Observer'):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: ConcreteSubject):
        if subject.state < 10:
            print("ConcreteObserverA: Reacted to state < 10")

class ConcreteObserverB(Observer):
    def update(self, subject: ConcreteSubject):
        if subject.state >= 10:
            print("ConcreteObserverB: Reacted to state >= 10")

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    print("[UI] Setting state to 5:")
    subject.state = 5
    # ConcreteObserverA: Reacted to state < 10

    print("[UI] Setting state to 15:")
    subject.state = 15
    # ConcreteObserverB: Reacted to state >= 10
