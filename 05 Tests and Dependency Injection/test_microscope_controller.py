import unittest
from mock_microscope import MockMicroscope
from microscope_controller import MicroscopeController

class TestMicroscopeController(unittest.TestCase):
    def test_scan_raster(self):
        mock_microscope = MockMicroscope()
        controller = MicroscopeController(mock_microscope)

        controller.scan_raster(rows=2, cols=2, step_size=5, zoom_level=2.0)

        expected_commands = [
            # First row (2 columns)
            "move_x(5)", "move_y(5)",
            "move_x(5)", "move_y(5)",
            "move_z(1)",  # End of first row

            # Second row (2 columns)
            "move_x(5)", "move_y(5)",
            "move_x(5)", "move_y(5)",
            "move_z(1)",  # End of second row

            "zoom(2.0)"
        ]

        self.assertEqual(mock_microscope.commands, expected_commands)

if __name__ == "__main__":
    unittest.main()
