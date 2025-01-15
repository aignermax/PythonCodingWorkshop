class SingletonMeta(type):
    """
    Metaclass that ensures only one instance of the class exists.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    """
    Example of a Logger that should only exist once.
    """
    def __init__(self):
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)

    def show_logs(self):
        for msg in self.logs:
            print(msg)

if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("First message")
    logger2.log("Second message")

    # Both references should be the same instance
    print(logger1 is logger2)  # True
    logger1.show_logs()
