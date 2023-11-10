from Rectangle import Rectangle

class Surface():
    def __init__(self, filename, x, y, h, w):
        """
        Initializing a surface object

        Args:
            filename (_type_): _description_
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            h (int): height of the rectangle
            w (int): width of the rectangle
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)
    
    def getRect(self):
        """
        Takes the arguments and creates a rectangle 

        Returns:
            Rectangle: returns the rectangle attribute 
        """
        return self.rect