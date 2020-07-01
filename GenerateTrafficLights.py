from itertools import cycle, islice
from Lights import TrafficLight
import threading

from datetime import datetime


class GenerateTraffic:
    def __init__(self, number):
        self.number = number
        self.counter = 1

        self.colours = ["red", "green", "white"]
        self.colours_modified = list(islice(cycle(self.colours), number))

        self.traffic_whole = []
        for i, x in zip(range(number), self.colours_modified):
            self.traffic_whole.append(TrafficLight(x, "off", i + 1))

    def runProgram(self):
        threading.Timer(1.0, self.runProgram).start()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        for light in self.traffic_whole:
            if light.position == self.counter:
                light.state = "on"
            if light.position == self.counter-1 :
                light.state = "off"
        print(current_time + str(self.traffic_whole) + " counter:" + str(self.counter))
        if self.counter == self.number:
            light.state = "off"
            self.counter = 1
        else:
            self.counter = self.counter + 1









        # for light in self.traffic_whole:
        #     #turn light on if equal to currrent counter
        #     if light.position == self.counter:
        #         light.state = "on"
        #     #turn light off if equal to previous counter
        #     if light.position == self.counter-1 :
        #         light.state = "off"
        #     if self.counter == 4:
        #         light.state = "off"
        #         self.counter = 0



