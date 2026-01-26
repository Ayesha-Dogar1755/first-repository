import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self,radius):
        return math.pi*radius*radius
class Rectangle(Shape):   
    def area(self,length,width):
        return length*width
class Triangle(Shape):
    def area(self,base,height):
        return 0.5*base*height
circle1=Circle()
print("Area of Circle:",circle1.area(5))
rectangle1=Rectangle()
print("Area of Rectangle:",rectangle1.area(4,6))
triangle1=Triangle()
print("Area of Triangle:",triangle1.area(3,8))

    
