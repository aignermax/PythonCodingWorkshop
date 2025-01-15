# isp_bad.py

from abc import ABC, abstractmethod

class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_doc(self, doc: str):
        pass

    @abstractmethod
    def scan_doc(self) -> str:
        pass

    @abstractmethod
    def fax_doc(self, doc: str):
        pass

class BasicPrinter(MultiFunctionDevice):
    """
    BasicPrinter can print, but cannot scan or fax.
    Yet it must implement all methods -> violates ISP.
    """
    def print_doc(self, doc: str):
        print(f"Printing: {doc}")

    def scan_doc(self) -> str:
        raise NotImplementedError("This device cannot scan")

    def fax_doc(self, doc: str):
        raise NotImplementedError("This device cannot fax")
