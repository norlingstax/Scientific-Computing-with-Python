class Rectangle:
    def __init__(self, w, h):
        self.width=w
        self.height=h
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)
    def set_width(self, w_n):
        self.width=w_n
    def set_height(self, h_n):
        self.height=h_n
    def get_area (self):
        return self.width*self.height
    def get_perimeter(self):
        return (self.width+self.height)*2
    def get_diagonal(self):
        return ((self.width**2+self.height**2)**0.5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*'*self.width+'\n')*self.height
    def get_amount_inside (self, shape):
        st = self.width // shape.width
        nd = self.height // shape.height
        return st*nd
        

class Square (Rectangle):
    def __init__(self, side):
        self.width=side
        self.height=side
    def __str__(self):
        return 'Square(side={})'.format(self.width)
    def set_width(self, side):
        self.width=side
    def set_height(self, side):
        self.height=side
    def set_side(self,side):
        self.width=side
        self.height=side