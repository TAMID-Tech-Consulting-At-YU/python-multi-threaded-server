from abc import ABC, abstractmethod


class Member(ABC):

    def __init__(self, name, grad_year, major):
        self.name = name
        self.grad_year = grad_year
        self.major = major

    @abstractmethod
    def get_major(self):
        return self.major

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def get_graduation_year(self):
        return self.grad_year

    def __repr__(self):
        return f"Member=({self.name},{self.major},{self.grad_year})"
