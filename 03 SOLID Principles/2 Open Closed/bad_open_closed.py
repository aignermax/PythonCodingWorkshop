# ocp_bad.py

class DiscountCalculator:
    def calculate(self, price: float, discount_type: str) -> float:
        if discount_type == "percentage":
            return price * 0.9  # 10% off
        elif discount_type == "fixed":
            return price - 5
        else:
            # If we need a new discount type, we add a new 'elif' -> modifies existing class
            return price

if __name__ == "__main__":
    calc = DiscountCalculator()
    print(calc.calculate(100, "percentage"))  # 90
    print(calc.calculate(100, "fixed"))       # 95
