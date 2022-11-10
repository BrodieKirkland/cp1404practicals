"""Project Class"""
import datetime


class Project:
    """Project Class"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Meant to compare start_date's"""
        date_string = self.start_date
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        other_date_string = other.start_date
        other_date = datetime.datetime.strptime(other_date_string, "%d/%m/%Y").date()
        return date < other_date
