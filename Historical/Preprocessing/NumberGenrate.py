# ----------------------- Normal Day
def am415_545am():
    import random
    numbers_car = [random.randint(60, 100) for _ in range(7)]
    numbers_bike = [random.randint(10, 30) for _ in range(7)]
    numbers_bus = [random.randint(10, 25) for _ in range(7)]
    numbers_truck = [random.randint(5, 20) for _ in range(7)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def six_nineAm():
    import random
    numbers_car = [random.randint(100, 150) for _ in range(13)]
    numbers_bike = [random.randint(25, 60) for _ in range(13)]
    numbers_bus = [random.randint(25, 35) for _ in range(13)]
    numbers_truck = [random.randint(0, 10) for _ in range(13)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])
def am915_1045am():
    import random
    numbers_car = [random.randint(30, 80) for _ in range(7)]
    numbers_bike = [random.randint(10, 20) for _ in range(7)]
    numbers_bus = [random.randint(0, 30) for _ in range(7)]
    numbers_truck = [random.randint(15, 30) for _ in range(7)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def Am11_1PM():
    import random
    numbers_car = [random.randint(30, 90) for _ in range(9)]
    numbers_bike = [random.randint(5, 20) for _ in range(9)]
    numbers_bus = [random.randint(10, 20) for _ in range(9)]
    numbers_truck = [random.randint(25, 35) for _ in range(9)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def pm115_345pm():
    import random
    numbers_car = [random.randint(45, 100) for _ in range(11)]
    numbers_bike = [random.randint(10, 30) for _ in range(11)]
    numbers_bus = [random.randint(10, 35) for _ in range(11)]
    numbers_truck = [random.randint(5, 20) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def pm4_pm630():
    import random
    numbers_car = [random.randint(100, 140) for _ in range(11)]
    numbers_bike = [random.randint(25, 40) for _ in range(11)]
    numbers_bus = [random.randint(20, 40) for _ in range(11)]
    numbers_truck = [random.randint(5, 10) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Pm645_945pm():
    import random
    numbers_car = [random.randint(50, 100) for _ in range(13)]
    numbers_bike = [random.randint(15, 30) for _ in range(13)]
    numbers_bus = [random.randint(7, 20) for _ in range(13)]
    numbers_truck = [random.randint(10, 25) for _ in range(13)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Pm10_4am():
    import random
    numbers_car = [random.randint(15, 25) for _ in range(25)]
    numbers_bike = [random.randint(0, 2) for _ in range(25)]
    numbers_bus = [random.randint(0, 2) for _ in range(25)]
    numbers_truck = [random.randint(10, 30) for _ in range(25)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


# ---------------------------------------------- Friday

def Am415_9AmF():
    import random
    numbers_car = [random.randint(20, 60) for _ in range(20)]
    numbers_bike = [random.randint(0, 20) for _ in range(20)]
    numbers_bus = [random.randint(0, 10) for _ in range(20)]
    numbers_truck = [random.randint(20, 40 ) for _ in range(20)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Am9_3PmF():
    import random
    numbers_car = [random.randint(80,120) for _ in range(24)]
    numbers_bike = [random.randint(20,50) for _ in range(24)]
    numbers_bus = [random.randint(5,30) for _ in range(24)]
    numbers_truck = [random.randint(5,20) for _ in range(24)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Pm3_7PmF():
    import random
    numbers_car = [random.randint(40,60) for _ in range(16)]
    numbers_bike = [random.randint(5,25) for _ in range(16)]
    numbers_bus = [random.randint(10,15) for _ in range(16)]
    numbers_truck = [random.randint(5,20) for _ in range(16)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def pm7_10pmF():
    import random
    numbers_car = [random.randint(20,60) for _ in range(11)]
    numbers_bike = [random.randint(0,10) for _ in range(11)]
    numbers_bus = [random.randint(0,10) for _ in range(11)]
    numbers_truck = [random.randint(15,25) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def Pm10_4amF():
    import random
    numbers_car = [random.randint(29, 45) for _ in range(25)]
    numbers_bike = [random.randint(0, 3) for _ in range(25)]
    numbers_bus = [random.randint(0, 3) for _ in range(25)]
    numbers_truck = [random.randint(15, 45) for _ in range(25)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

# ---------------------- normal day
am415_545am()
six_nineAm()
am915_1045am()
Am11_1PM()
pm115_345pm()
pm4_pm630()
Pm645_945pm()
Pm10_4am()


# ------------- Friday

Am415_9AmF()
Am9_3PmF()
Pm3_7PmF()
pm7_10pmF()
Pm10_4amF()