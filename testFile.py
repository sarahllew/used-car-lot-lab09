from Car import *
from CarInventory import *
from CarInventoryNode import *

# Car.py tests
def test_Carfunctions():
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Toyota", "Prius", 2015, 2000)
    c2 = Car("Toyota", "Tacoma", 2015, 1000)
    c3 = Car("Mercedes", "E450", 2019, 9000)
    c4 = Car("Ford", "Ranger", 2021, 2500)
    c5 = Car("FOrD", "RaNgEr", 2021, 2500)
    
    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"
    assert str(c1) == "Make: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000"
    assert str(c2) == "Make: TOYOTA, Model: TACOMA, Year: 2015, Price: $1000"
    assert str(c3) == "Make: MERCEDES, Model: E450, Year: 2019, Price: $9000"
    assert c < c1
    assert c2 > c1
    assert c < c2
    assert not(c3 > c1)
    assert not(c2 < c1)
    assert (c2 > c3)
    assert c3 < c2
    assert not(c4 > c3)
    assert c4 == c5

# CarInventoryNode.py Tests
def test_CarInventoryNode():
    c = Car("HOndA", "CRV", 2007, 8000)
    c1 = Car("Toyota", "PriUs", 2015, 2000)
    c2 = Car("toyota", "TACOMA", 2015, 1000)
    carNode = CarInventoryNode(c)
    assert str(carNode) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\n"
    carNode.cars.append(c1)
    assert str(carNode) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\n"
    carNode.cars.append(c2)
    assert str(carNode) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\nMake: TOYOTA, Model: TACOMA, Year: 2015, Price: $1000\n"
    c3 = Car("Dodge", "dart", 2010, 6000)
    c4 = Car("dodge", "DaRt", 2003, 5000)
    carNode2 = CarInventoryNode(c3)
    carNode2.cars.append(c4) 
    assert str(carNode2) == "Make: DODGE, Model: DART, Year: 2010, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n"

# CarInventoryNode.py Tests
def test_CarInventoryNode():
    bst1 = CarInventory()
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Toyota", "Prius", 2015, 2000)
    c2 = Car("Toyota", "Tacoma", 2015, 1000)
    c3 = Car("Mercedes", "E450", 2019, 9000)
    c11 = Car("MeRcEdes", "E450", 2014, 25000)
    c4 = Car("Ford", "Ranger", 2021, 2500)
    c5 = Car("FOrD", "RaNgEr", 2021, 2501)

    bst1.addCar(c)
    bst1.addCar(c1)
    bst1.addCar(c2)
    bst1.addCar(c3)
    bst1.addCar(c4)
    bst1.addCar(c5)
    bst1.addCar(c11)

    assert bst1.getBestCar("Honda", "CRV") == c
    assert bst1.getBestCar("Toyota", "Prius") == c1
    assert bst1.getBestCar("Ford","Ranger") == c5
    assert bst1.getBestCar("Mercedes", "E450") == c3
    assert bst1.getWorstCar("Nissan", "Leaf") == None
    assert bst1.getWorstCar("Mercedes", "E450") == c11
    assert bst1.getBestCar("Honda", "Accord") == None

    bst2 = CarInventory()
    c6 = Car("Nissan", "Leaf", 2018, 18000)
    c7 = Car("Tesla", "Model3", 2018, 50000)
    c8 = Car("Mercedes", "Sprinter", 2022, 40000)
    c9 = Car("Mercedes", "Sprinter", 2014, 25000)
    c10 = Car("Ford", "Ranger", 2021, 25000)   

    bst2.addCar(c6)
    bst2.addCar(c7)
    bst2.addCar(c8)
    bst2.addCar(c9)
    bst2.addCar(c10)

    assert bst2.getBestCar("Nissan", "Leaf") == c6
    assert bst2.getBestCar("Mercedes", "Sprinter") == c8
    assert bst2.getBestCar("Ford","Ranger") == c10
    assert bst2.getBestCar("Honda", "Accord") == None
    assert bst2.getWorstCar("Nissan", "Leaf") == c6
    assert bst2.getWorstCar("Mercedes", "Sprinter") == c9
    assert bst2.getBestCar("Honda", "Accord") == None

# Part Two Tests for Used Car

def test_getSuccessor():
    '''test the general case and case used for BST maintenance'''

    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getSuccessor("Mazda", "CX-5") == "Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.getSuccessor("BMW", "X5") == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"
    assert bst.getSuccessor("Audi", "A3") == "Make: BMW, Model: X5, Year: 2022, Price: $60000\nMake: BMW, Model: X5, Year: 2020, Price: $58000\n"
    assert bst.getSuccessor("Tesla", "CX-5") == None


def test_removeCarinOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.inOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000"

    bst2 = CarInventory()
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Toyota", "Prius", 2015, 2000)
    c2 = Car("Toyota", "Prius", 2015, 1000)
    c3 = Car("Mercedes", "E450", 2019, 9000)
    c4 = Car("Ford", "Ranger", 2021, 2500)

    bst2.addCar(c)
    bst2.addCar(c1)
    bst2.addCar(c2)
    bst2.addCar(c3)
    bst2.addCar(c4)

    bst2.removeCar("Toyota","Prius", 2015, 2000)
    assert bst2.inOrder() == "Make: FORD, Model: RANGER, Year: 2021, Price: $2500\nMake: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: MERCEDES, Model: E450, Year: 2019, Price: $9000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\n"

    bst2.removeCar("Mercedes", "E450", 2019, 9000)
    assert bst2.inOrder() == "Make: FORD, Model: RANGER, Year: 2021, Price: $2500\nMake: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\n"

    
def test_removeCarpreOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW","X5",2020, 58000)
    assert bst.preOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000"
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.preOrder() == "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000"


    bst2 = CarInventory()
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Toyota", "Prius", 2015, 2000)
    c2 = Car("Toyota", "Prius", 2015, 1000)
    c3 = Car("Mercedes", "E450", 2019, 9000)
    c4 = Car("Ford", "Ranger", 2021, 2500)
    bst2.addCar(c)
    bst2.addCar(c1)
    bst2.addCar(c2)
    bst2.addCar(c3)
    bst2.addCar(c4)

    bst2.removeCar("Ford", "Ranger", 2021, 2500)
    assert bst2.preOrder() == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\nMake: MERCEDES, Model: E450, Year: 2019, Price: $9000\n"
    bst2.removeCar("Honda", "CRV", 2007, 8000)
    assert bst2.preOrder() == "Make: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\nMake: MERCEDES, Model: E450, Year: 2019, Price: $9000\n"

def test_removeCarpostOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.postOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000"
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.postOrder() == "Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000"

    bst2 = CarInventory()
    c = Car("Honda", "CRV", 2007, 8000)
    c1 = Car("Toyota", "Prius", 2015, 2000)
    c2 = Car("Toyota", "Prius", 2015, 1000)
    c3 = Car("Mercedes", "E450", 2019, 9000)
    c4 = Car("Ford", "Ranger", 2021, 2500)
    bst2.addCar(c)
    bst2.addCar(c1)
    bst2.addCar(c2)
    bst2.addCar(c3)
    bst2.addCar(c4)

    bst2.removeCar("Ford", "Ranger", 2021, 2500)
    assert bst2.postOrder() == "Make: MERCEDES, Model: E450, Year: 2019, Price: $9000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\nMake: HONDA, Model: CRV, Year: 2007, Price: $8000\n"
    bst2.removeCar("Honda", "CRV", 2007, 8000)
    assert bst2.postOrder() == "Make: MERCEDES, Model: E450, Year: 2019, Price: $9000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $2000\nMake: TOYOTA, Model: PRIUS, Year: 2015, Price: $1000\n"



