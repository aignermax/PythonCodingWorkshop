# srp_bad.py

class Order:
    """
    This Order class is responsible for:
    1. Handling the order data (items, prices).
    2. Printing the order details (UI).
    3. Saving the order to a file (data persistence).
    This violates the Single Responsibility Principle.
    """
    def __init__(self, items: list[dict]):
        self.items = items  # e.g., [{"name": "Widget", "price": 9.99}, ...]

    def calculate_total(self) -> float:
        return sum(item['price'] for item in self.items)

    def print_order(self) -> None:
        # UI logic
        print("Order details:")
        for item in self.items:
            print(f" - {item['name']} at ${item['price']}")
        print(f"Total: ${self.calculate_total()}")

    def save_order(self, filename: str) -> None:
        # Data persistence
        with open(filename, "w") as f:
            f.write("Order details:\n")
            for item in self.items:
                f.write(f" - {item['name']} at ${item['price']}\n")
            f.write(f"Total: ${self.calculate_total()}\n")

# Example usage
if __name__ == "__main__":
    order = Order([{"name": "Widget", "price": 9.99}, {"name": "Gadget", "price": 12.99}])
    order.print_order()
    order.save_order("order.txt")
