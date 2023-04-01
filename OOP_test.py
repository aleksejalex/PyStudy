# short file description, like coding utf8, author, date

def print_hi(name: str) -> None:
    """
    function description goes here
    (we don't have to specify types of vars, but it's nice
    practice, especially in case if OOP, when functions
    accept and return objects of unusual type (like myCat etc.)
    Important: python won't crash if we abandon those specifications.
    :param name: name (str)
    """
    print(f'Hi, {name}')
    return None  # no functionality, just for illustration


class Cat:
    latin_name = "Felinae"  # class atribute. It's same for all Cats, unchangeable

    def __init__(self, name: str, age: int, mass: float, tail_length: float):
        """
        Constructor of a Cat on given properties of a cat
        :param name: name (str)
        :param age: age (int) in years
        :param mass: mass (float) in kilograms
        :param tail_length: tail length (float) in cm
        """
        self.name = name
        self.age = age
        self.mass = mass
        self.tail_length = tail_length

    def get_bmi(self) -> float:
        """
        calculates Body Mass Index of a cat
        :return: BMI (float in %)
        """
        length_of_cat = self.tail_length * 1.8  # let's assume tail is 80% of cat's length
        bmi = self.mass / ( length_of_cat ** 2 )
        return bmi

    def __repr__(self) -> str:
        """revoked when print(Object) is called"""
        return f"Meow! I'm {self.name} and I'm {self.age} y.o."


if __name__ == '__main__':  # like calling main function in C++
    print_hi('PyCharm')

    Kitty = Cat("Kitty", 3, 5.5, 13)  # 3 y.o., 5.5kg, 13cm tail
    print(Kitty)
    print(Kitty.get_bmi())

    Chloe = Cat("Chloe", 2.5, 13, 12.8)  # 2 y.o., 13kg, 12.8cm tail
    print(Chloe)
    print(Chloe.get_bmi())



