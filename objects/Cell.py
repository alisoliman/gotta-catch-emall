class Cell():

    def __init__(self, location=None):
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.location = location
        self.has_pokemon = False

