from Vechile import *
#slot class
class Slot:

    def __init__(self,slotid,type,status):
        self.slotid = slotid
        self.type = type
        self.status = status
    def enter(self,Vechile):
        self.Vechile = Vechile


    def exit(self,slotno,Vechile):
        self.Vechile = None
