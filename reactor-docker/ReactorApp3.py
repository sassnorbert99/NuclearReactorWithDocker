import threading
import time


class Reactor:
    def __init__(self): #példányszintű = self
        self.uran235 = 1000000000
        self.split = 1
        self.xenon = 0
        self.xenon_start = 0
        self.temperature = 0
        self.temperature_start = 0
        self.rods = 80
        self.produce = 0
        self.water = 100
        self.steam = 100 - self.water
        self.counter = 0
        self.operate = False

    def start_reactor(self):
        self.operate = True
        produce_thread = threading.Thread(target=self.calculate_produce)
        produce_thread.start()
        input_thread = threading.Thread(target=self.i_o_request)
        input_thread.start()


        while self.uran235 > 0 and self.operate:
            reduction = 1 - (self.rods / 100) - self.xenon_start - self.temperature_start
            if reduction < 0:
                reduction = 0
            atom = self.split * self.split * reduction
            self.xenon += atom
            self.uran235 = self.uran235 - self.xenon - atom

            if self.temperature >= 20000:
                self.steam = 100
                self.water = 100 - self.steam
            elif self.temperature > 100:
                self.steam = self.water * self.temperature / 20000
                self.water = 100 - self.steam
            else:
                self.steam = 0
                self.water = 100 - self.steam

            """
            warning system, if the system was overheated:
            """
            if atom <= 0 and self.temperature > 30000:
                self.temperature *= 0.99  # 1%-al lehűl minden ciklusban

            if self.water >= 5:
                self.temperature -= 100
            if self.temperature >= 10000 and self.water >= 5:
                self.temperature = 10000
            if atom > 0:
                self.temperature += 200 + self.split
            if self.temperature <= 1000:
                self.temperature_start = 0
            if self.temperature <= 0:
                self.temperature = 0
            if self.xenon <= 1000:
                self.xenon_start = 0
            if self.temperature > 1000:
                self.xenon = 0
                self.temperature_start = self.temperature * 0.00000833
            if self.xenon > 1000:
                self.xenon_start = self.xenon * 0.00000833

            self.split += 1

            print("Control rods: " + str(self.rods) + "%; Xenon: " + str(int(self.xenon)) + "; Temperature: " + str(
                int(self.temperature)) + " -> reduction: " + str(round(reduction, 2)) + "; water: " + str(
                round(self.water, 2)) + "; steam: " + str(round(self.steam, 2)))
            if self.steam > 0:
                self.produce += 400 * self.steam / 100
            delay = 1 - reduction
            self.counter += 1
            time.sleep(delay)

        if self.uran235 == 0:
            print("uranium chamber is empty!")
        produce_thread.join()
        input_thread.join()


    def stop_reactor(self):
        self.operate = False

    def calculate_produce(self):
        value = 0
        while self.operate:
            time.sleep(1.0)
            print("produce per second: " + str(round(self.produce - value, 2)))
            value = self.produce


    def i_o_request(self):
        while self.operate:
            i_o = input()
            if i_o == "i" and self.rods >= 0 and self.rods < 100:
                #emeli a rodokat 10-el
                self.rods += 10
                print("pushing rods by 10%")
            elif i_o == "o" and self.rods > 0 and self.rods < 100:
                #csökkenti a rodokat 10-el
                self.rods -= 10
                print("pulling out rods by 10%")
            elif i_o == "s":
                self.rods = 100










