class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f'"Куб размером {self.width}х{self.height}"'
        else:
            return f'"Прямоугольник размером {self.width}x{self.height}"'

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"
q3 = Quadrilateral(4, 7)
print(q3)