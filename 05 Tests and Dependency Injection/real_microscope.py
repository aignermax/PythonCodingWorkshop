from microscope_interface import MicroscopeInterface

class RealMicroscope(MicroscopeInterface):
    """
    A concrete class that represents the real, physical microscope.
    In a real-world scenario, each method would contain
    the hardware-specific commands to move/zoom the microscope.
    """

    def move_x(self, steps: int) -> None:
        print(f"[RealMicroscope] Moving X by {steps} steps.")

    def move_y(self, steps: int) -> None:
        print(f"[RealMicroscope] Moving Y by {steps} steps.")

    def move_z(self, steps: int) -> None:
        print(f"[RealMicroscope] Moving Z by {steps} steps.")

    def zoom(self, level: float) -> None:
        print(f"[RealMicroscope] Zooming to {level}x.")
