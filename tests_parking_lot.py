#!/usr/bin/env python3

import unittest

from src.parking_lot import ParkingLot


class ParkingLotTest(unittest.TestCase):
    def setUp(self):
        self.parking_lot_new = ParkingLot(capacity=6)

    def test_class_params(self):

        self.assertEqual(self.parking_lot_new.capacity, 6)
        self.assertEqual(self.parking_lot_new.slots_occupied, [None] * 6)
        self.assertEqual(self.parking_lot_new.cars_parked, set())
        self.assertEqual(self.parking_lot_new.slots_available, 6)

    def test_allot_slot(self):

        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-1111", "White"),
            "Allocated slot number: {}".format(1),
        )
        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-2222", "Blue"),
            "Allocated slot number: {}".format(2),
        )
        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-3333", "Green"),
            "Allocated slot number: {}".format(3),
        )
        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-4444", "White"),
            "Allocated slot number: {}".format(4),
        )
        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-5555", "Blue"),
            "Allocated slot number: {}".format(5),
        )
        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-6666", "White"),
            "Allocated slot number: {}".format(6),
        )

        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-6666", "White"),
            "KA-01-HH-6666 Car is already parked",
        )

        self.assertEqual(
            self.parking_lot_new.allot_slot("KA-01-HH-9999", "White"),
            "Sorry, parking lot is full",
        )

    def test_leave_slot(self):

        self.parking_lot_new.allot_slot("KA-01-HH-1111", "White")

        self.assertEqual(
            self.parking_lot_new.leave_slot(1),
            "Slot number 1 is free")

        self.assertEqual(
            self.parking_lot_new.leave_slot(1), "Slot number 1 is already free"
        )

    def test_status(self):

        self.parking_lot_new.allot_slot("KA-01-HH-1111", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-2222", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-3333", "Blue")

        expected_ans = "Slot No.    Registration No    Colour\n"
        expected_ans += "1           KA-01-HH-1111      White\n"
        expected_ans += "2           KA-01-HH-2222      White\n"
        expected_ans += "3           KA-01-HH-3333      Blue\n"

        self.assertEqual(
            self.parking_lot_new.parking_lot_status(),
            expected_ans)

    def test_car_registration_nos_for_colour(self):

        self.parking_lot_new.allot_slot("KA-01-HH-1111", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-2222", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-3333", "Blue")

        self.assertEqual(
            self.parking_lot_new.car_registration_nos_for_colour("White"),
            (True, ["KA-01-HH-1111", "KA-01-HH-2222"]),
        )
        self.assertEqual(
            self.parking_lot_new.car_registration_nos_for_colour("Blue"),
            (True, ["KA-01-HH-3333"]),
        )
        self.assertEqual(
            self.parking_lot_new.car_registration_nos_for_colour("Black"),
            (False, "No cars found of colour Black"),
        )

    def test_slots_occupied_by_colour(self):

        self.parking_lot_new.allot_slot("KA-01-HH-1111", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-2222", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-3333", "Blue")

        self.assertEqual(
            self.parking_lot_new.slots_occupied_by_colour("White"),
            (True, [1, 2])
        )

        self.assertEqual(
            self.parking_lot_new.slots_occupied_by_colour("Blue"), (True, [3])
        )

        self.assertEqual(
            self.parking_lot_new.slots_occupied_by_colour("Black"),
            (False, "No cars found of colour Black"),
        )

    def test_car_slot_no_for_registration_no(self):

        self.parking_lot_new.allot_slot("KA-01-HH-1111", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-2222", "White")
        self.parking_lot_new.allot_slot("KA-01-HH-3333", "Blue")

        self.assertEqual(
            self.parking_lot_new.car_slot_no_for_registration_no(
                "KA-01-HH-1111"), 1
        )

        self.assertEqual(
            self.parking_lot_new.car_slot_no_for_registration_no(
                "KA-01-HH-9999"), "Not found",
        )

    def test_process(self):

        self.assertEqual(
            self.parking_lot_new.process("park KA-01-HH-1234 White".split()),
            "Allocated slot number: {}".format(1),
        )

        expected_ans = "Slot No.    Registration No    Colour\n"
        expected_ans += "1           KA-01-HH-1234      White\n"

        self.assertEqual(
            self.parking_lot_new.process("status".split()),
            expected_ans)

        self.assertEqual(
            self.parking_lot_new.process(
                "registration_numbers_for_cars_with_colour White".split()
            ),
            "KA-01-HH-1234",
        )

        self.assertEqual(
            self.parking_lot_new.process(
                "slot_number_for_registration_number KA-01-HH-1234".split()
            ),
            1,
        )

        self.assertEqual(
            self.parking_lot_new.process(
                "slot_number_for_registration_number KA-01-HH-9999".split()
            ),
            "Not found",
        )

        self.assertEqual(
            self.parking_lot_new.process(
                "leave 1".split()), "Slot number 1 is free"
        )


if __name__ == "__main__":
    unittest.main()
