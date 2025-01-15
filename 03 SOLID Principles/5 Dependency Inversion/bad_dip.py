# dip_bad.py

class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL Database...")

    def fetch_data(self):
        return ["data1", "data2"]

class DataAnalyzer:
    """
    High-level module depends directly on
    a concrete low-level class (MySQLDatabase).
    """
    def __init__(self):
        self.db = MySQLDatabase()

    def analyze(self):
        self.db.connect()
        data = self.db.fetch_data()
        print(f"Analyzing {data}")
