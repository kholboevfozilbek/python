
from turtle import clear


class Footballer:

    def __init__(self, name="", club="", position="", number=0):
        self.name = name
        self.club = club
        self.position = position
        self.number = number

    def display(self):
        print("Player:", self.__name)
        print("Club:", self.__club)
        print("Position:", self.__position)
        print("Number:", self.__number)


Salah = Footballer("Mohammad Salah", "Liverpool", "Right Forward", 11)

print(getattr(Salah, "club"))

