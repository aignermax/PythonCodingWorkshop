from microscope_interface import MicroscopeInterface

class MicroscopeController:
    """
    High-level logic that uses a microscope (any that implements MicroscopeInterface).
    Demonstrates Dependency Injection: the specific microscope implementation
    (real or mock) is injected via the constructor.
    """
    def __init__(self, microscope: MicroscopeInterface):
        self.microscope = microscope

    def scan_raster(self, rows: int, cols: int, step_size: int, zoom_level: float):
        """
        Example method: moves the microscope in a raster pattern (rows x cols)
        and then sets a certain zoom level.
        """
        for r in range(rows):
            for c in range(cols):
                self.microscope.move_x(step_size)
                self.microscope.move_y(step_size)
            self.microscope.move_z(1)  # Move Z up by 1 after each row

        self.microscope.zoom(zoom_level)
