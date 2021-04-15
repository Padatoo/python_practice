class Vector:
    def __init__(self, *args):
        self.values = [i for i in args if isinstance(i, int)]
        #print(self.values)
        #print(self.values)

    def __str__(self):
        if self.values:
            return f"Вектор{tuple(sorted(self.values))}"
        else:
            return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[x + y for x, y in zip(self.values, other.values)])
                #return self.values
            else:
                raise TypeError("Сложение векторов разной длины недопустимо")
            #print(self.values)
        elif isinstance(other, int):
                return Vector(*[x + other for x in self.values])
        else:
            raise TypeError(f"Вектор нельзя сложить с <{other}>")
        #print(self.values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[x * y for x, y in zip(self.values, other.values)])
            else:
                raise TypeError("Умножение векторов разной длины недопустимо")
        elif isinstance(other, int):
            return Vector(*[x * other for x in self.values])
        else:
            raise TypeError(f"Вектор нельзя умножать с <{other}>")


#a = Vector(12, 3, 5)
#b = Vector(11, 3, 4)
#a + b
v1 = Vector(1,2,3)
v2 = Vector(3,4,5)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"