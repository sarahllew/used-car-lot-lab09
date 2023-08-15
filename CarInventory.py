
from Car import *
from CarInventoryNode import *

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0 

    def addCar(self, car):
        if self.root:
            self._add(car,self.root)
        else:
            self.root = CarInventoryNode(car)
        self.size += 1

    def _add(self, car, currentNode):
        if car.model == currentNode.cars[0].model and car.make == currentNode.cars[0].make:
            currentNode.cars.append(car)
        elif car < currentNode.cars[0]:
            if currentNode.getLeft() != None:
                self._add(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car)
                currentNode.left.parent = currentNode
        else:
            if currentNode.getRight() != None:
                self._add(car, currentNode.right)
            else:
                currentNode.right = CarInventoryNode(car)
                currentNode.right.parent = currentNode
         
    def doesCarExist(self, car): 
        a = self.find(car.make, car.model, self.root)
        if a != None:
            for x in a.cars:
                if x == car:
                    return True
        return False   

    def _inOrder(self, node):
        ret = ""
        if node != None:
            ret += self._inOrder(node.getLeft())
            ret += str(node)
            ret += self._inOrder(node.getRight())
        return ret 
    
    def inOrder(self):
        if self != None:
            return self._inOrder(self.root)
        else:
            return ""

    def _preOrder(self, node):
        ret = ""
        if node != None:
            ret += str(node)
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())
        return ret 
            
    def preOrder(self):
        if self != None:
            return self._preOrder(self.root)
        else:
            return ""
        
    def _postOrder(self, node):
        ret = ""
        if node != None:
            ret += self._postOrder(node.getLeft())
            ret += self._postOrder(node.getRight())
            ret += str(node)
        return ret

    def postOrder(self):
        ret = ""
        if self != None:
            return self._postOrder(self.root)
        else:
            return ""
        
    def find(self, make, model, node):
        #return the node with the same make and model
        if node == None:
            return None
        elif make.upper() == node.getMake() and model.upper() == node.getModel():
            return node
        elif make.upper() < node.getMake() or (make.upper() == node.getMake() and model.upper() < node.getModel()):
            return self.find(make, model, node.getLeft())
        else:
            return self.find(make, model, node.getRight())
        
    def getBestCar(self, make, model): 
        a = self.find(make, model, self.root)
        if a != None:
            bestCar = a.cars[0]
            for i in a.cars:
                if bestCar < i:
                    bestCar = i
            return bestCar
        else:
            return None
        
    def getWorstCar(self, make, model):  
        a = self.find(make, model, self.root)
        if a != None:
            worstCar = a.cars[0]
            for i in a.cars:
                if worstCar > i:
                    worstCar = i
            return worstCar
        else:
            return None

    def getTotalInventoryPrice(self):  
        if self.root != None:
            return self._total(self.root)

        else:
            return 0
        
    def _total(self, node):
        total = 0
        for x in node.cars:
            total += x.price
        if node.getRight() != None:
            total += self._total(node.getRight())
        if node.getLeft() != None:
            total += self._total(node.getLeft())
        return total

    def getSuccessor(self, make, model):
        a = self.find(make, model, self.root)
        succ = None
        if self.root == None:
            return None
        elif a == None:
            return None
        elif a.getRight() != None:
            succ = a.right.findMin()
        else:
            if a.parent:
                if a.isLeftChild():
                    succ = a.parent
                else:
                    a.parent.right = None
                    succ = self.getSuccessor(a.parent.make, a.parent.model)
                    a.parent.right = a
        return succ

    def removeCar(self, make, model, year, price):
        ''' attempts to find the car with specified model, make, year, price and
            removes it from the CarInventoryNode's cars list.
            if the list empty after removing the car, remove the node entirely.
            returns True if the car is successfully removed,
            and False if the car is not present.'''
        a = self.find(make, model, self.root)
        x = Car(make, model, year, price)
        if a == None:
            return False
        if a != None:
            if x in a.cars:
                a.cars.remove(x)
                self.size = self.size - 1
                if len(a.cars) == 0:
                    self._remove(a,x)
                return True 
            return False

    def _remove(self, current, car):
        # removing the car from the list 
        if len(current.cars) > 1:
            for i in range(len(current.cars)-1):
                    if i == car:
                        current.cars.remove(i)

        # removing the entire node 
        if len(current.cars) == 0:
                # Case 1: the node is a leaf 
            if not (current.right or current.left):
                if current.parent == None:
                    self.root = None
                elif current == current.parent.left:
                    current.parent.left = None
                else:
                    current.parent.right = None
                    
                # Case 3: the node has both children
            elif current.right and current.left: 
                succ = self.getSuccessor(current.getMake(), current.getModel())
                succ.spliceOut()
                current.cars = succ.cars
                current.make = succ.make
                current.model = succ.model
                # Case 2: the node has one child only 
            else:
                if current.getLeft() != None:
                    if current.parent == None:
##                        current.replaceNode(current.left.make,
##                                            current.left.model,
##                                            current.left.cars,
##                                            current.left.left,
##                                            current.left.right)
                        self.root = current.left
                        current.left.parent = None
                    elif current.isLeftChild():
                        current.left.parent = current.parent
                        current.parent.left = current.left
                    else:
                        current.left.parent = current.parent
                        current.parent.right = current.left
    ##                  else:
    ##                      # change self.root # and make the parent none
                else:
                    if current.parent == None:
##                        current.replaceNode(current.right.make,
##                                            current.right.model,
##                                            current.right.cars,
##                                            current.right.left,
##                                            current.right.right)
                        self.root = current.right
                        current.right.parent = None
                    elif current.isLeftChild():
                        current.right.parent = current.parent
                        current.parent.left = current.right
                    else:
                        current.right.parent = current.parent
                        current.parent.right = current.right


##
##bst.removeCar("BMW", "X5", 2020, 58000)
##
###                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
###                                 /                                       \
###           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
###                   /
###  Audi,A3,[Car(Audi,A3,2021,25000)]
##
##assert bst.inOrder() == \
##"""\
##Make: AUDI, Model: A3, Year: 2021, Price: $25000
##Make: BMW, Model: X5, Year: 2022, Price: $60000
##Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
##Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
##"""
##
##bst.removeCar("BMW", "X5", 2022, 60000)
##
###                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
###                                 /                                       \
###           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
##
##
##assert bst.inOrder() == \
##"""\
##Make: AUDI, Model: A3, Year: 2021, Price: $25000
##Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
##Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
##"""
##
####bst.removeCar("BMW", "X5", 2020, 58000)
####
#####                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#####                                 /                                       \
#####           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#####                   /
#####  Audi,A3,[Car(Audi,A3,2021,25000)]
####
####assert bst.preOrder() == \
####"""\
####Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
####Make: BMW, Model: X5, Year: 2022, Price: $60000
####Make: AUDI, Model: A3, Year: 2021, Price: $25000
####Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
####"""
##
##bst.removeCar("BMW", "X5", 2022, 60000)
##
###                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
###                                 /                                       \
###           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
##
##
##assert bst.preOrder() == \
##"""\
##Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
##Make: AUDI, Model: A3, Year: 2021, Price: $25000
##Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
##"""
####
####bst.removeCar("BMW", "X5", 2020, 58000)
####
#####                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#####                                 /                                       \
#####           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#####                   /
#####  Audi,A3,[Car(Audi,A3,2021,25000)]
####
####assert bst.postOrder() == \
####"""\
####Make: AUDI, Model: A3, Year: 2021, Price: $25000
####Make: BMW, Model: X5, Year: 2022, Price: $60000
####Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
####Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
####"""
##
##bst.removeCar("BMW", "X5", 2022, 60000)
##
###                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
###                                 /                                       \
###           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
##
##
##assert bst.postOrder() == \
##"""\
##Make: AUDI, Model: A3, Year: 2021, Price: $25000
##Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
##Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
##"""
##                
##                    
                        
                    



