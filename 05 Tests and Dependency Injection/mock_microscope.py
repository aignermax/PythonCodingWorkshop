from microscope_interface import MicroscopeInterface

class MockMicroscope(MicroscopeInterface):
    """
    A mock/fake microscope used for testing. It doesn't move real hardware.
    Instead, it just stores the commands for verification in tests.
    """
    def __init__(self):
        self.commands = []

    def move_x(self, steps: int) -> None:
        self.commands.append(f"move_x({steps})")

    def move_y(self, steps: int) -> None:
        self.commands.append(f"move_y({steps})")

    def move_z(self, steps: int) -> None:
        self.commands.append(f"move_z({steps})")

    def zoom(self, level: float) -> None:
        self.commands.append(f"zoom({level})")
