from abc import ABC, abstractmethod

class MicroscopeInterface(ABC):
    """
    An interface (abstract base class) for microscope operations.
    """
    @abstractmethod
    def move_x(self, steps: int) -> None:
        pass

    @abstractmethod
    def move_y(self, steps: int) -> None:
        pass

    @abstractmethod
    def move_z(self, steps: int) -> None:
        pass

    @abstractmethod
    def zoom(self, level: float) -> None:
        pass
