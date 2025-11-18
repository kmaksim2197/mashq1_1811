class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.__grades:
            self.__grades.remove(grade)

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_grades(self):
        return list(self.__grades)


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"


animals = [Dog(), Cat(), Cow()]

for a in animals:
    print(a.speak())
