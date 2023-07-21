class Rectangle:
    def __init__(self, width, height) : 
        self.height = height
        self.width = width
    def __str__ (self) :
        string = f"Rectangle(width={self.width}, height={self.height})"
        return string

    def set_width(self,width) : 
        self.width = width
        return
    def set_height(self,height) : 
        self.height = height
        return
    def get_area(self) : 
        area = self.width *self.height
        return area
    def get_perimeter(self) : 
        perimeter = 2* self.width + 2* self.height 
        return perimeter
    def get_diagonal(self) :
        diagonal = (self.width **2 + self.height**2) **0.5
        return diagonal
    def get_picture(self) :
        if self.height > 50 or self.width > 50 : 
            return "Too big for picture."
        height = self.height
        width = self.width
        picture = ""
        while height > 0: 
            width = self.width
            while width > 0: 
                picture +="*"
                width -=1
            picture += "\n"
            height -= 1
        return picture
    def get_amount_inside(self, otherShape) : 
        heightRatio = round(self.height / otherShape.height)
        widthRatio = round(self.width / otherShape.width)
        numberOfTimes = heightRatio * widthRatio
        return numberOfTimes

class Square(Rectangle): 
    def __init__(self, side):
        self.height = side
        self.width = side
    def __str__(self):
        return f"Square(side={self.width})"
        
    def set_side(self,side):
        self.width = side
        self.height = side



