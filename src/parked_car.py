class ParkedCar(object):
    def __init__(self, reg_id, slot, colour):

        """
        Class used to create an entry of car to be parked with
        reg_id [STRING]: registration id
        slot [INT]: slot number
        colour [STRiNG]: colour of the car
        """
        self.reg_id = reg_id
        self.slot = slot
        self.colour = colour
