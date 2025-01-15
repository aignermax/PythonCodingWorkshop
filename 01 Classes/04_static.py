class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

class Counter:
    # Klassenvariable (in anderen Sprachen „static“ genannt)
    count = 0

    def __init__(self):
        Counter.count += 1

if __name__ == "__main__":
    # Statische Methode aufrufen
    result = MathUtils.add(5, 7)
    print(f"5 + 7 = {result}")  # Ausgabe: 5 + 7 = 12

    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    print(f"Anzahl der Instanzen: {Counter.count}")  # Ausgabe: Anzahl der Instanzen: 3
