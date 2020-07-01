from itertools import cycle, islice

class TrafficLight:

    def __init__(self, colour, state, position):
        self.position = position
        self.colour = colour
        self.state = state

    def __repr__(self):
        return "Traffic Lights({},{},{})".format(self.colour, self.state, self.position)