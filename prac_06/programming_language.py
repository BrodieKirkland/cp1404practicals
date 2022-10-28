"""Programming Language class"""


class ProgrammingLanguage:
    """Programming Language class"""
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Print name, typing, reflection, year"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"

    def is_dynamic(self):
        """Check if is dynamic"""
        return self.typing.lower() == "dynamic"


