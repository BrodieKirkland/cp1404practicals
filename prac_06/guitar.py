"""
Guitars!
Time estimate: 60 minutes
actual:

Guitar class
"""


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : ${self.cost:,.2f})"

    def get_age(self, base_year: int):
        """Get age starting from base_year"""
        return base_year - self.year

    def is_vintage(self, base_year):
        """Check if over 50 years old"""
        return self.get_age(base_year) >= 50
