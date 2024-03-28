class President:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def introduce(self):
        print(f"I am {self.name}, the President of {self.country}.")

# Trying to create multiple instances of the President
president1 = President("John Doe", "United States")
president1.introduce()  # Output: I am John Doe, the President of United States.

president2 = President("Jane Smith", "United States")
president2.introduce()  # Output: I am John Doe, the President of United States.

print(president1 is president2)  # Output: True
