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
        self.isOne = False

        self.colours_list = ["Red Light", "Green Light", "White Light"]
        col_length = len(self.colours_list)

        self.colours_modified = []
        for x in range(0, self.number):
            self.colours_modified.append(self.colours_list[x % col_length])

        # self.colours_modified = list(islice(cycle(self.colours_list), number))

        self.traffic_whole = []
        for i, x in zip(range(number), self.colours_modified):
            self.traffic_whole.append(TrafficLight(x, "off", i))

    def runProgram(self):
        # threading.Timer(1.0, self.runProgram).start()
        while(True):
            index = 0
            light = self.traffic_whole
            current_time = datetime.now().strftime("%H:%M:%S:%f")
            while index < len(light):
                # time.sleep(1)
                #initial variable
                if light[index].position == self.counter:
                    time.sleep(1)
                    # print("counter: " + str(self.counter))
                    # print("number:" + str(self.number))
                    # print("index: " + str(index))

                    light[index].state = "on"
                    print(current_time + " " + str(light[index]))
                #turn of behind initial variable from 0-len(9)
                elif light[index].position == self.counter - 1:# and (self.counter-1) >= 0 and self.counter < self.number:
                    # print("counter: " + str(self.counter))
                    # print("number:" + str(self.number))
                    # print("index: " + str(index))

                    light[index].state = "off"
                    print(current_time + " " + str(light[index]))
                #reach end of loop
                elif self.counter == self.number:
                    # print("counter: " + str(self.counter))
                    # print("number:" + str(self.number))
                    # print("index: " + str(index))

                    light[self.counter - 1].state = "off"
                    self.counter = 0
                    index = -1
                    print(current_time + " " + str(light[index]))
                index += 1

            # print("---")
            self.counter += 1
            # time.sleep(1)

    # def runProgram(self):
    #
    #     while(True):
    #         i = 0
    #         for light in self.traffic_whole:
    #             #if position == [1,2,3], turn on
    #             if light.position == self.counter:
    #                 light.state = "on"
    #                 print(light)
    #             elif light.position == self.counter - 1 and (self.counter-1) >= 0 and self.counter < self.number:
    #                 light.state = "off"
    #                 print(light)
    #             elif self.counter == self.number:
    #                 self.counter = 0
    #                 print(light)
    #             else:
    #                 #pass
    #                 print(light)
    #
    #         self.counter += 1
    #         print("---")
    #
    #
    #         time.sleep(1)







    # def runProgram(self):
    #     threading.Timer(1.0, self.runProgram).start()
    #     current_time = datetime.now().strftime("%H:%M:%S:%f")
    #     for light in self.traffic_whole:
    #
    #         if self.number == 1:
    #             self.isOneTrafficLight(light)
    #         else:
    #             # print states that are on
    #             if light.position == self.counter:
    #                 light.state = "on"
    #                 print(current_time + " " + str(light) + " counter: " + str(self.counter) +" " +str(self.number))
    #             # print states behind counter
    #             elif light.position == self.counter - 1:
    #                 light.state = "off"
    #                 print(current_time + " " + str(light) + " counter: " + str(self.counter) + " " + str(self.number))
    #
    #
    #
    #
    #             # print("")
    #     #
    #     # self.printWholeArray(current_time)
    #
    #     if self.counter == self.number:
    #         light.state = "off"
    #         self.counter = 1
    #
    #         print((datetime.now()).strftime("%H:%M:%S:%f") + " " + str(light) + " counter: " + str(self.counter) + " " + str(self.number))
    #
    #     else:
    #         self.counter = self.counter + 1



    def printWholeArray(self, current_time):
        print(current_time + " " + str(self.traffic_whole) + " counter:" + str(self.counter))

    def isOneTrafficLight(self, light):
        if not self.isOne:
            light.state = "on"
            self.isOne = True
        elif self.isOne:
            light.state == "off"
            self.isOne = False
