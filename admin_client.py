import Good
from Good import *

items = []
basket = []
basket_items = []

dv = Computer("Macbook pro 13", 900000, 30, "corei7", 16, 418, 1000)
sm = SmartPhone("xiomi redmi note 5", 90000, 30, "corei5", 16, 4, 5)
lp = Laptop("IPAD", 500000, 40, "corei5", 4, 120, 1000, 10, 7)

items.append(dv)
items.append(sm)
items.append(lp)


def addData(items, quantity):
    for j in range(quantity):
        model = str(input("ENTER THE MODEL: "))
        price = float(input("ENTER THE PRICE: "))
        count = int(input("ENTER THE COUNT: "))
        items.append(Device(model, price, count, "corei3", 4))


def printData(items):
    for j in range(len(items)):
        print(j, "", items[j].showDetails())


def searchItems(items, word):
    for j in range(len(items)):
        if items[j].getName() == word:
            print(items[j].showDetails())




def filterLessPrice(items):
    price = int(input("ENTER THE PRICE: "))
    for j in range(len(items)):
        if items[j].getPrice() < price:
            print(items[j].showDetails())


def filterMorePrice(items):
    price = int(input("ENTER THE PRICE: "))
    for j in range(len(items)):
        if items[j].getPrice() > price:
            print(items[j].showDetails())


def filterCpu(items):
    cpu = str(input("ENTER THE CPU: "))
    for j in range(len(items)):
        if items[j].getCpu() == cpu:
            print(items[j].showDetails())


def filterRam(items):
    ram = int(input("ENTER THE RAM: "))
    for j in range(len(items)):
        if items[j].getRam() == ram:
            print(items[j].showDetails())




def buyItems(items):
    for i in range(len(items)):
        print(i, "", items[i].showDetails())
    itemToBuy = int(input("WHAT DO U WANT BUY?: "))
    for j in range(len(items)):
        if itemToBuy == j:
            items[j].iterSold()
            items[j].iterCountNeg()
            basket.append(items[j].getPrice())
            basket_items.append(items[j].getPriceItems())
            print("YOU BUY ", items[j].showDetails())


# functions for admin
def addItems(items):
    print("ENTER 1 FOR ADD SMARTPHONE")
    print("ENTER 2 FOR ADD COMPUTER")
    print("ENTER 3 FOR ADD LAPTOP")
    items_press = int(input(": "))
    if items_press == 1:
        model = str(input("ENTER THE MODEL: "))
        price = str(input("ENTER THE PRICE: "))
        count = int(input("ENTER THE COUNT: "))
        cpu = str(input("ENTER THE CPU: "))
        ram = int(input("ENTER THE RAM: "))
        mgpx = int(input("ENTER THE MGPX: "))
        generation = int(input("ENTER THE GENERATION: "))
        items.append(SmartPhone(model, price, count, cpu, ram, mgpx, generation))
    if items_press == 2:
        model = str(input("ENTER THE MODEL: "))
        price = str(input("ENTER THE PRICE: "))
        count = int(input("ENTER THE COUNT: "))
        cpu = str(input("ENTER THE CPU: "))
        ram = int(input("ENTER THE RAM: "))
        ssd = int(input("ENTER THE SSD: "))
        memory = int(input("ENTER THEMEMORY: "))
        items.append(Computer(model, price, count, cpu, ram, ssd, memory))
    if items_press == 3:
        model = str(input("ENTER THE MODEL: "))
        price = str(input("ENTER THE PRICE: "))
        count = int(input("ENTER THE COUNT: "))
        cpu = str(input("ENTER THE CPU: "))
        ram = int(input("ENTER THE RAM: "))
        ssd = int(input("ENTER THE SSD: "))
        memory = int(input("ENTER THEMEMORY: "))
        weight = int(input("ENTER THE WEIGHT: "))
        touch = int(input("ENTER THE TOUCH: "))
        items.append(Laptop(model, price, count, cpu, ram, ssd, memory, weight, touch))


def updateQuantity(items):
    printData(items)
    itemUpdate = int(input("WHAT DO U WANNA UPDATE?: "))
    for j in range(len(items)):
        if itemUpdate ==  j:
            count = int(input("ENTER THE COUNT FOR UPDATE: "))
            items[j].setCount(count)

def deleteItems(items):
    printData(items)
    itemDelete = int(input("WHAT DO U WANNA DELETE?: "))
    for j in range(len(items)):
        if itemDelete == j:
            del items[j]


def outIncomeReport(items):
    income_sum = 0
    for j in range(len(basket)):
        income_sum += basket[j]
    print("ITEMS FOR INCOME REPORT: ")
    for j in range(len(basket_items)):
        print(basket_items[j])
    print("INCOME: ",income_sum)


def outIncomeReport2(items):
    income_sum = 0
    for j in range(len(basket)):
        income_sum += basket[j]
    print("RESULT: ")
    for j in range(len(basket_items)):
        print(basket_items[j])
    print("YOU SHOULD PAY: ",income_sum)

while True:
    print("PRESS 1 IF YOU CLIENT")
    print('PRESS 2 IF YOU ADMIN')
    print('PRESS 0 FOR EXIT')
    control = int(input(": "))
    if control ==1:
        print("--------CLIENT PANEL-------")
        print("PRESS 1 FOR LIST ITEMS")
        print("PRESS 2 FOR FIND ITEMS")
        print("PRESS 3 FOR FILTER")
        print("PRESS 4 FOR BUY")
        print("PRESS 5 FOR VIEW CART")
        print("PRESS 0 FOR EXIT")

        client_press = int(input(":"))
        if client_press == 1:
            for j in range(len(items)):
                print(items[j].showDetails()," feature: ",items[j].getPerfomance())
        elif client_press == 2:
            word = str(input("ENTER THE WORD FOR THE FIND: "))
            searchItems(items, word)
        elif client_press == 3:
            print("ENTER 1 FOR FILTER MONEY MORE")
            print("ENTER 2 FOR FILTER MONEY LESS")
            print("ENTER 3 FOR FILTER CPU")
            print("ENTER 4 FOR FILTER RAM")
            filterPress = int(input(":"))

            if filterPress == 1:
                print("LIST FOR FILTER MONEY MORE")
                filterMorePrice(items)
            elif filterPress == 2:
                print("LIST FOR FILTER MONEY LESS")
                filterLessPrice(items)
            elif filterPress == 3:
                print("LIST FOR FILTER CPU")
                filterCpu(items)
            elif filterPress == 4:
                print("LIST FOR FILTER RAM")
                filterRam(items)
        elif client_press == 4:
            buyItems(items)
            printData(items)
            outIncomeReport2(items)
        elif client_press == 5:
            outIncomeReport2(items)
        elif client_press == 0:
            print("--------EXIT-------")
            continue

    elif control == 2:
        print("--------ADMIN PANEL-------")
        print("PRESS 1 FOR ADD ITEMS")
        print("PRESS 2 FOR UPDATE QUANTITY ITEMS")
        print("PRESS 3 FOR DELETE ITEMS")
        print("PRESS 4 FOR INCOME REPORT ")
        print("PRESS 0 FOR EXIT")
        admin_press = int(input(":"))

        if admin_press == 1:
            addItems(items)
            printData(items)
        elif admin_press == 2:
            updateQuantity(items)
            printData(items)
        elif admin_press == 3:
            deleteItems(items)
            printData(items)
        elif admin_press == 4:
            outIncomeReport(items)
        elif admin_press == 0:
            print("--------EXIT-------")
            continue

    elif control == 0:
        print("--------EXIT FROM PROGRAM--------")
        break