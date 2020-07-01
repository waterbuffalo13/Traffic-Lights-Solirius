
class TrafficLight:

    def __init__(self, colour, state, position):
        self.colour = colour
        self.state = state
        self.position = position


    def __repr__(self):
        return "Traffic Lights({},{},{})".format(self.colour, self.state, self.position)


