class Good:

    def __init__(self, model, price, count):
        self.price = price
        self.model = model
        self.count = count
        self.sold = 0

    def setCount(self, count):
        self.count = count

    def iterSold(self):
        self.sold += 1

    def iterCountNeg(self):
        self.count -= 1

    def getPrice(self):
        return self.price

    def getPriceItems(self):
        return f"model:{self.model} | price:{self.price} | sold:{self.sold}"

    def getName(self):
        return self.model

    def setSold(self, sold):
        self.sold = sold

    def showDetails(self):
        return f"price:{self.price} | model:{self.model} | count:{self.count}"


class Device(Good):

    def __init__(self, model, price, count, cpu, ram):
        super().__init__(model, price, count)
        self.cpu = cpu
        self.ram = ram

    def getCpu(self):
        return self.cpu

    def getRam(self):
        return self.ram

    def getPerfomance(self):

        if self.cpu == "corei3" and self.ram == 4:
            return f"Рабочий на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "corei5" and self.ram >= 4:
            return f"Универсальный на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "corei7" and self.ram >= 8:
            return f"Игровой на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "corei9" and self.ram >= 16:
            return f"Ультра мощьный на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "a3" and self.ram == 1:
            return f"Рабочий на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "a4" and self.ram >= 2:
            return f"Универсальный на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "a6" and self.ram >= 3:
            return f"Игровой на базе {self.cpu} и {self.ram} RAM"
        elif self.cpu == "a10" and self.ram >= 4:
            return f"Ультра мощьный на базе {self.cpu} и {self.ram} RAM"


class SmartPhone(Device):

    def __init__(self, model, price, count, cpu, ram, mgpx, generation):
        super().__init__(model, price, count, cpu, ram)
        self.mgpx = mgpx
        self.generation = generation


class Computer(Device):

    def __init__(self, model, price, count, cpu, ram, ssd, memory):
        super().__init__(model, price, count, cpu, ram)
        self.ssd = ssd
        self.memory = memory


class Laptop(Computer):

    def __init__(self, model, price, count, cpu, ram, ssd, memory, weight, touch):
        super().__init__(model, price, count, cpu, ram, ssd, memory)
        self.weight = weight
        self.touch = touch

