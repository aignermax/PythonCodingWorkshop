# isp_refactored.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self, doc: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self) -> str:
        pass

class Fax(ABC):
    @abstractmethod
    def fax_doc(self, doc: str):
        pass

class BasicPrinter(Printer):
    def print_doc(self, doc: str):
        print(f"Printing: {doc}")

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print_doc(self, doc: str):
        print(f"Printing: {doc}")

    def scan_doc(self) -> str:
        return "Scanned content"

    def fax_doc(self, doc: str):
        print(f"Faxing: {doc}")
