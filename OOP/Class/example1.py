
class Footballer:

    def __init__(self, name="", club="", position="", number=0):
        self.__name = name
        self.__club = club
        self.__position = position
        self.__number = number

    def display(self):
        print("Player:", self.__name)
        print("Club:", self.__club)
        print("Position:", self.__position)
        print("Number:", self.__number)


Salah = Footballer("Mohammad Salah", "Liverpool", "Right Forward", 11)

print(Salah.club)


