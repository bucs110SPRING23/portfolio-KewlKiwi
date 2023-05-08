

class Rectangle:

    def __init__(self, x=0, y=0, h=0, w=0):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    
    def __str__(self):
        return str(self.x, self.y, self.width, self.height)

