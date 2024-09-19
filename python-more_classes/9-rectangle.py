#!/usr/bin/python3
#!/usr/bin/python3
"""Module for a class Rectangle"""


class Rectangle:
    """class rectangle"""
    number_of_instances = 0  # class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initalization of instance attrib"""
        self.width = width
        self.height = height  # instance attribute
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if not isinstance(value, int):  # verify if value is a int class
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__height = value

    def area(self):
        """Calcul and return area"""
        return self.width * self.height

    def perimeter(self):
        """Calcul perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''Returns a string representation of the rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) *
                        self.width for _ in range(self.height))  # use _ if index is not important

    def __repr__(self):
        '''Returns a string representation of the rectangle'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle or rect_1 if they are equal"""
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():  # for method use () -> area()
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Check if rectangle is a Square"""
        return cls(size, size)  # like (width = 5, height = 5)
