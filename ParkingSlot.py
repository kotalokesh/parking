from Slot import *
from mysqlpark import *
class Parking:
    slots=[]
    def loadslots(self): #method to load slots initially
        mycursor.execute('select slotid,type,status from Slot  ')
        result = mycursor.fetchall()
        for x in result:
            s = Slot(x[0],x[1],x[2])
            self.slots.append(s)
            print(s.slotid , s.type,s.status)
    def getavilability(self,type): #metod to get the status of the slots
        for s in self.slots:
            if s.type == type and s.status == 'yes':
                print("yes u can park at ",s.slotid)
                break
        else:
            print("ther are no avilable slots")

    def park(self,slotid,Vechile): #to park the vechile
        self.slots[slotid - 1].enter(Vechile)
        enter(slotid)
        vechileenter(Vechile,slotid)
    def exit(self,slotid,number):#mothod to exit the vechile
        exit(slotid)
        vechileexit(number)

    def display(self,slotid):
        for i in self.slots:
            if i.slotid == slotid:
                i.Vechile.display()

