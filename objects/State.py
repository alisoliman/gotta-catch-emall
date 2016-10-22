class State():
    def __init__(self, cell, orientation, pokes, time_left_to_hatch):
        self.cell = cell
        self.orientation = orientation
        self.num_pokemons = pokes
        self.time_left_to_hatch = time_left_to_hatch

    def __str__(self):
        return 'cell {} , {}, has {} pokemons, time: {}'.format(self.cell, self.orientation, str(self.num_pokemons), str(self.time_left_to_hatch))