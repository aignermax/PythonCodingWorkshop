# dip_refactored.py

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_data(self) -> list[str]:
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL Database...")

    def fetch_data(self) -> list[str]:
        return ["data1", "data2"]

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL Database...")

    def fetch_data(self) -> list[str]:
        return ["dataA", "dataB"]

class DataAnalyzer:
    """
    High-level module depends on an abstraction (Database),
    not a specific database implementation.
    """
    def __init__(self, db: Database):
        self.db = db

    def analyze(self):
        self.db.connect()
        data = self.db.fetch_data()
        print(f"Analyzing {data}")

# Example usage
if __name__ == "__main__":
    mysql_db = MySQLDatabase()
    pg_db = PostgreSQLDatabase()

    analyzer1 = DataAnalyzer(mysql_db)
    analyzer1.analyze()

    analyzer2 = DataAnalyzer(pg_db)
    analyzer2.analyze()
