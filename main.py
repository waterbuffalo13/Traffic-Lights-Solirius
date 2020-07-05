from GenerateTrafficLights import GenerateTraffic

if __name__ == '__main__':
    while True:
        try:
            x = int(input("How many traffic lights do you want to generate?"))
            GenerateTraffic(x).runProgram()
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")


