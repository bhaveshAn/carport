#!/usr/bin/env python3

import sys

try:
    from parking_lot import ParkingLot
except ImportError:
    from .parking_lot import ParkingLot


def main(filename=None):

    """
    This function is used to initialize parking lot
    and executing all instructions depending on the mode.
    Two modes are as follows:
    1. File Mode: requires filename to be passed
    2. Interactive mode: Command prompt based shell
    """

    if filename:
        # Used for File Mode
        with open(filename) as f:
            content = f.readlines()
            content = [x.strip() for x in content]

        first_line = content[0].split()
        output = []
        if first_line[0] == "exit":
            sys.exit()
        elif first_line[0] == "create_parking_lot":
            parking_lot_new = ParkingLot(int(first_line[1]))
            output.append(
                "Created a parking lot with {} slots".format(
                    first_line[1]))

        if not content[1:]:
            return "No Instructions Found"

        for line in content[1:]:
            if line == "exit":
                break
            output.append(parking_lot_new.process(line.split()))

        for l in output:
            print(l)
        sys.exit()
    else:
        # Used for Interactive Mode
        inp = input("$ ").strip().split()
        if inp[0] == "exit":
            sys.exit()
        elif inp[0] == "create_parking_lot":
            parking_lot_new = ParkingLot(int(inp[1]))
            print("Created a parking lot with {} slots".format(inp[1]))

        else:
            print("No Parking Lot Found")

        inp = input("$ ").strip().split()
        while inp:
            if inp == "exit":
                sys.exit()
            print(parking_lot_new.process(inp))
            inp = input("$ ").strip().split()


if __name__ == "__main__":

    if len(sys.argv) > 1:
        main(filename=sys.argv[1])
    else:
        main()
