from itertools import cycle, islice
from Lights import TrafficLight

class GenerateTraffic:
    def __init__(self, count):
        traffic_whole = []
        colours = ["red", "green", "white"]
        colours_gen = list(islice(cycle(colours), count))

        for i, x in zip(range(count), colours_gen):
            traffic_whole.append(TrafficLight(x, "off", i + 1))
        print(traffic_whole)