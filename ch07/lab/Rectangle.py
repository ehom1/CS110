class Rectangle():
    def __init__(self, x, y, h, w):
        """
        Initializing a rectangle object

        Args:
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            h (int): height of the rectangle 
            w (int): width of the rectangle 
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
        
    def __str__(self):
        """_summary_

        Returns:
            str: returns the arguments 
        """
        return f"(x: {self.x} y: {self.y}) height: {self.height}, width: {self.width}"