# srp_refactored.py

class Order:
    """
    Only responsible for managing order data and
    basic calculations (e.g., total price).
    """
    def __init__(self, items: list[dict]):
        self.items = items

    def calculate_total(self) -> float:
        return sum(item['price'] for item in self.items)


class OrderPrinter:
    """Handles how an order is presented (UI/Output)."""
    @staticmethod
    def print_order(order: Order) -> None:
        print("Order details:")
        for item in order.items:
            print(f" - {item['name']} at ${item['price']}")
        print(f"Total: ${order.calculate_total()}")


class OrderSaver:
    """Responsible for persisting the order data to a file."""
    @staticmethod
    def save_order(order: Order, filename: str) -> None:
        with open(filename, "w") as f:
            f.write("Order details:\n")
            for item in order.items:
                f.write(f" - {item['name']} at ${item['price']}\n")
            f.write(f"Total: ${order.calculate_total()}\n")

# Example usage
if __name__ == "__main__":
    order = Order([{"name": "Widget", "price": 9.99}, {"name": "Gadget", "price": 12.99}])
    OrderPrinter.print_order(order)
    OrderSaver.save_order(order, "order.txt")
