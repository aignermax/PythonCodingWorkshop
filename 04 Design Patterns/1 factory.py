class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")

class Square(Shape):
    def draw(self):
        print("Drawing a square...")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape_type: {shape_type}")

if __name__ == "__main__":
    # Client code:
    factory = ShapeFactory()
    shape1 = factory.create_shape("circle")
    shape2 = factory.create_shape("square")

    shape1.draw()  # Drawing a circle...
    shape2.draw()  # Drawing a square...
