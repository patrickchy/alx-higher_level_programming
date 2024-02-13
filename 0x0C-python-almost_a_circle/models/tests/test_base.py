#!/usr/bin/python3
"""contains test cases for the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test for the base class"""

    b1 = Base()
    b2 = Base()
    b3 = Base()
    b4 = Base(12)
    b5 = Base()
    b6 = Base(-1)
    b7 = Base("string")
    b8 = Base(0)

    def test_first_increment(self):
        self.assertEqual(self.b1.id, 1)

    def test_second_increment(self):
        self.assertEqual(self.b2.id, 2)

    def test_third_increment(self):
        self.assertEqual(self.b3.id, 3)

    def test_id_not_none(self):
        self.assertEqual(self.b4.id, 12)

    def test_fourth_increment(self):
        self.assertEqual(self.b5.id, 4)

    def test_negative_id(self):
        self.assertEqual(self.b6.id, -1)

    def test_string_id(self):
        self.assertEqual(self.b7.id, "string")

    def test_id_0(self):
        self.assertEqual(self.b8.id, 0)


if __name__ == "__main__":
    unittest.main()
