try:
    from parked_car import ParkedCar
except ImportError:
    from .parked_car import ParkedCar


class ParkingLot(object):
    def __init__(self, capacity):

        """
        Class used to create parking lot with following specs:

        capacity [INT]: capacity of the parking lot
        slots_occupied [LIST]: Slots are occupied with respective data
        cars_parked [SET]: set of registration id of the parked cars
        slots_available [INT]: No. of slots available in the parking lot
        """

        self.capacity = capacity
        self.slots_occupied = [None] * capacity
        self.cars_parked = set()
        self.slots_available = capacity

    def allot_slot(self, car_reg_id, car_colour):

        """
        This method allows parking lot to allot a slot to car
        if slots available

        return: Alloted Slot Number
        """

        if car_reg_id in self.cars_parked:
            return "{} Car is already parked".format(car_reg_id)
        elif self.slots_available <= 0:
            return "Sorry, parking lot is full"

        i = 0

        while self.slots_occupied[i]:
            i += 1

        car = ParkedCar(reg_id=car_reg_id, colour=car_colour, slot=i + 1)

        self.slots_occupied[i] = car
        self.cars_parked.add(car.reg_id)
        self.slots_available -= 1
        return "Allocated slot number: {}".format(car.slot)

    def leave_slot(self, slot):

        """
        This method allows to leave a slot with given slot number

        return: Slot Number after free
        """

        if not self.slots_occupied[slot - 1]:
            return "Slot number {} is already free".format(slot)

        car = self.slots_occupied[slot - 1]
        self.slots_occupied[slot - 1] = None
        self.cars_parked.remove(car.reg_id)
        self.slots_available += 1
        return "Slot number {} is free".format(slot)

    def car_registration_nos_for_colour(self, colour):

        """
        This method allows to return list of cars with same colour as given

        return: List of registration numbers of cars if colour is found
        """

        cars = []

        for node in self.slots_occupied:
            if not node:
                continue
            if node.colour == colour:
                cars.append(node.reg_id)

        if cars:
            return True, cars
        return False, "No cars found of colour {}".format(colour)

    def slots_occupied_by_colour(self, colour):

        """
        This method allows to return slot of cars having same colour as given

        return: List of slots alloted to cars if colour is found
        """

        cars = []

        for node in self.slots_occupied:
            if not node:
                continue
            if node.colour == colour:
                cars.append(node.slot)
        if cars:
            return True, cars
        return False, "No cars found of colour {}".format(colour)

    def car_slot_no_for_registration_no(self, reg_id):

        """
        This method allows to find the slot occupied by a car
        given its registration no.

        return: Slot Number [INT]
        """

        if reg_id not in self.cars_parked:
            return "Not found"

        slot_number = 0

        for node in self.slots_occupied:
            if not node:
                continue
            if node.reg_id == reg_id:
                slot_number = node.slot
                break
        return slot_number

    def parking_lot_status(self):

        """
        This method returns the status of the Parking Lot

        return: Tabular Status of Parking Lot [STRING]
        """

        ans = "Slot No.    Registration No    Colour\n"

        for i in range(0, len(self.slots_occupied) - 1):
            if not self.slots_occupied[i]:
                continue
            ans += "{0}           {1}      {2}\n".format(
                self.slots_occupied[i].slot,
                self.slots_occupied[i].reg_id,
                self.slots_occupied[i].colour,
            )
        if self.slots_occupied[i + 1]:
            ans += "{0}           {1}      {2}".format(
                self.slots_occupied[i + 1].slot,
                self.slots_occupied[i + 1].reg_id,
                self.slots_occupied[i + 1].colour,
            )

        return ans

    def process(self, inp):

        """
        This method acts as driver method for the parking lot.
        It calls appropriate method depending on the given instruction.
        """

        if inp[0] == "park":
            return self.allot_slot(inp[1], inp[2])
        elif inp[0] == "leave":
            return self.leave_slot(int(inp[1]))
        elif inp[0] == "status":
            return self.parking_lot_status()
        elif inp[0] == "registration_numbers_for_cars_with_colour":
            is_found, res = self.car_registration_nos_for_colour(inp[1])
            if is_found:
                ans = ", ".join(res)
                return ans
            return res
        elif inp[0] == "slot_numbers_for_cars_with_colour":
            is_found, res = self.slots_occupied_by_colour(inp[1])
            if is_found:
                ans = ""
                if len(res) > 1:
                    ans += str(res[0])
                    for i in res[1:]:
                        ans += ", " + str(i)
                elif len(res) == 1:
                    ans += str(res[0])
                return ans
            return res
        elif inp[0] == "slot_number_for_registration_number":
            return self.car_slot_no_for_registration_no(inp[1])
        else:
            return "Invalid Instruction"
