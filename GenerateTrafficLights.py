from itertools import cycle, islice
from Lights import TrafficLight
import threading
import pandas as pd
from datetime import datetime, timedelta
import time


class GenerateTraffic:
    def __init__(self, number):
        self.number = number
        self.counter = 0

        self.colours_list = ["Red Light", "Green Light", "White Light"]
        self.colours_modified = []
        for x in range(0, self.number):
            self.colours_modified.append(self.colours_list[x % len(self.colours_list)])

        self.traffic_whole = []
        for i, x in zip(range(number), self.colours_modified):
            self.traffic_whole.append(TrafficLight(x, "off", i))

    def runProgram(self):
        # threading.Timer(1.0, self.runProgram).start()
        while(True):
            current_time = datetime.now().strftime("%H:%M:%S")

            if self.number == 1:
                for x in self.traffic_whole:
                    if x.state == "off":
                        x.state = "on"
                        print(current_time + " " + str(x))
                    else:
                        x.state = "off"
                        print(current_time + " " + str(x))
                    time.sleep(1)

            else:
                index = 0
                light = self.traffic_whole
                # current_time = datetime.now().strftime("%H:%M:%S")
                while index < len(light):
                    if light[index].position == self.counter:
                        time.sleep(1)
                        light[index].state = "on"
                        print(current_time + " " + str(light[index]))

                    #turn of behind initial variable from 0-len(9)
                    elif light[index].position == self.counter - 1:# and (self.counter-1) >= 0 and self.counter < self.number:
                        light[index].state = "off"

                        print(current_time + " " + str(light[index]))

                    #reach end of loop
                    elif self.counter == self.number:
                        light[self.counter - 1].state = "off"
                        self.counter = 0
                        index = -1

                        print(current_time + " " + str(light[index]))
                    else:
                        # print(current_time + " " + str(light[index]))
                        pass
                    index += 1
                self.counter += 1

