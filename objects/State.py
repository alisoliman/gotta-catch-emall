class State():
    def __init__(self, cell, orientation, pokes, time_left_to_hatch):
        self.cell = cell
        self.orientation = orientation
        self.num_pokemons = pokes
        self.time_left_to_hatch = time_left_to_hatch
