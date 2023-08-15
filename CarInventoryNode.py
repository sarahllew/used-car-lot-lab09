from Car import *

class CarInventoryNode:
    def __init__(self, car):
        self.cars = []
        self.car = car
        self.cars.append(car) # double check 
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        details = ""
        for i in self.cars:
            details += str(i) + "\n"
        return details
    
    def findMin(self):
        current = self
        while current.getLeft() != None:
            current = current.left
        return current

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def spliceOut(self):
        # Case 1:
        # if node to be removed is a leaf, set parents left or right
        # child refernece to None
        if not (self.right or self.left):
            if self.isLeftChild():
                self.parent.left = None # remove successor
            else:
                self.parent.right = None
        # Case 2
        # if node is not a leaf node. should only have a right child for
        # BST maintenance 
        elif self.right or self.left:
            if self.getRight() != None:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def replaceNode(self, make, model, car, lc, rc):
        self.make = make.upper()
        self.model = model.upper()
        self.cars = []
        self.car = car
        self.cars.append(car)
        self.left = lc
        self.right = rc
        if self.getLeft() != None:
            self.left.parent = self
        if self.getRight() != None:
            self.right.parent = self.replace
        
        

##car1 = Car("Dodge", "dart", 2015, 6000)
##car2 = Car("dodge", "DaRt", 2003, 5000)
##carNode = CarInventoryNode(car1)
##carNode.cars.append(car2)
##print(carNode)
##    
