class Location():

    def  __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: {}, y: {} ".format(self.x, self.y)