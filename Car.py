# Car.py

class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        '''car objects organized by lexicographical/alphabetical order of make
            if make is the same, then check model.
            if model is the same, then check year (least to greatest)
            if year is the same, organized by price (least to greatest)'''
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            elif self.model == rhs.model: # Car 2 > Car 1 if Car 2 is newer
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, rhs):
        if rhs is None:
            return False
        if self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price == rhs.price:
            return True
        else:
            return False

    def __str__(self):
        '''returns details in format "Make: [make], Model: [model], Year: [year], Price: $[price]".'''
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make.upper(), self.model.upper(), self.year, self.price)


