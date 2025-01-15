# ocp_refactored.py

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent  # e.g., 0.1 for 10%

    def apply(self, price: float) -> float:
        return price * (1 - self.percent)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount  # e.g., 5 for $5 off

    def apply(self, price: float) -> float:
        return price - self.amount

class DiscountCalculator:
    """
    Now we can extend with new DiscountStrategy
    classes without modifying DiscountCalculator.
    """
    def calculate(self, price: float, strategy: DiscountStrategy) -> float:
        return strategy.apply(price)

if __name__ == "__main__":
    calc = DiscountCalculator()

    # Percentage discount
    strategy1 = PercentageDiscount(0.1)
    print(calc.calculate(100, strategy1))  # 90

    # Fixed discount
    strategy2 = FixedDiscount(5)
    print(calc.calculate(100, strategy2))  # 95
