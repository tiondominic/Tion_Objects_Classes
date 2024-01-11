import math
print("This calculates both the area and circumference\ninput 0 to stop")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        print("The area of the Circle is: ", area)

    def circumference(self):
        circumference = 2 * math.pi * self.radius
        print("The circumference of the Circle is: ", circumference)


while True:
    Radius = eval(input("Enter radius of the circle: "))
    if Radius == 0:
        print("Have a nice day!")
        break

    circle = Circle(Radius)
    circle.area()
    circle.circumference()
    print("")
