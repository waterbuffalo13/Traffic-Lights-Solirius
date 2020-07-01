
class TrafficLight:

    def __init__(self, colour, state, position):
        self.colour = colour
        self.state = state
        self.position = position

    def __repr__(self):
        return "{} {} {}".format(self.position, self.colour, self.state)


