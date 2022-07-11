class Vechile:
    slotno = 0
    def __init__(self,type,number,name):
        self.type = type
        self.number = number
        self.name = name

    def display(self):
        print('type -',self.type)
        print('name -', self.name)








# vechile class
class Vechile:

    def __init__(self,type,name,colour,length,breadth):
        self.type = type
        self.name = name
        self.colour = colour
        self.length = length
        self.breadth = breadth
    def display(self):
        print('type -',self.type)
        print('name -', self.name)
        print('colour -', self.colour)

