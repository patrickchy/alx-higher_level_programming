#!/usr/bin/python3
"""test fot square class"""
import unittest
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """This defines the tests cases"""

    def setUp(self):
        self.obj = Square(1, 2, 3, 4)

    def test_size_width(self):
        self.assertEqual(self.obj.width, 1)

    def test_size_height(self):
        self.assertEqual(self.obj.height, 1)

    def test_x(self):
        self.assertEqual(self.obj.x, 2)

    def test_y(self):
        self.assertEqual(self.obj.y, 3)

    def test_id(self):
        self.assertEqual(self.obj.id, 4)

    def test_size_strings(self):
        with self.assertRaises(TypeError):
            obj = Square("1", 2, 3, 4)

    def test_x_strings(self):
        with self.assertRaises(TypeError):
            obj = Square(1, "2", 3, 4)

    def test_y_strings(self):
        with self.assertRaises(TypeError):
            obj = Square(1, 2, "3", 4)

    def test_id_strings(self):
        obj = Square(1, 2, 3, "4")
        self.assertEqual(obj.id, "4")

    def test_width_float(self):
        with self.assertRaises(TypeError):
            obj = Square(0.1, 2, 3, 4)

    def test_height_float(self):
        with self.assertRaises(TypeError):
            obj = Square(0.1, 2, 3, 4)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            obj = Square(1, 0.1, 3, 4)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            obj = Square(1, 2, "0.3", 4)


"""
    def test_id_as_string(self):

        self.assertEqual(self.r4.id, "5")

    def test_id_as_0(self):

        self.assertEqual(self.r5.id, 0)

    def test_id_as_neg(self):

        self.assertEqual(self.r6.id, -1)

    def test_width_not_int(self):

        with self.assertRaises(TypeError):
            Square("1", 2, 3, 4, 5)

    def test_neg_width(self):
        with self.assertRaises(ValueError):
            Square(-1, 2, 3, 4, 5)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 4, 5)

    # Error handling cases for height ====================================

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Square(1, "2", 3, 4, 5)

    def test_neg_height(self):
        with self.assertRaises(ValueError):
            Square(1, -1, 3, 4, 5)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Square(1, 0, 3, 4, 5)

    # Error handling cases for x ===============================

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3", 4, 5)

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3, 4, 5)

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, "4", 5)

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, 3, -4, 5)

    # Check for x and y values as 0 ===============================
    def test_x_zero(self):
        self.assertEqual(self.r7.x, 0)

    def test_y_zero(self):
        self.assertEqual(self.r8.y, 0)

    # Test for area ==========================
    def test_2_int(self):
        my_obj = Square(1, 2, 3, 4, 5)
        self.assertEqual(self.my_obj.area(), 2)

    def test_neg_int(self):
        with self.assertRaises(ValueError):
            my_obj = Square(-1, -2, 3, 4, 5)
            my_obj.area()

    def test_mixed_int(self):
        with self.assertRaises(ValueError):
            my_obj = Square(-1, 2, 3, 4, 5)
            my_obj.area()

    def test_0_int(self):
        with self.assertRaises(ValueError):
            my_obj = Square(0, 0, 3, 4, 5)
            my_obj.area()

    def test_strings(self):
        with self.assertRaises(TypeError):
            my_obj = Square("1", "2", 3, 4, 5)
            my_obj.area()

    def test_float(self):
        with self.assertRaises(TypeError):
            my_obj = Square(1.5, 2.5, 3, 4, 5)
            my_obj.area()

    def test_display_1(self):
        my_obj = Square(1, 1)

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            my_obj.display()
            printed_result = captured_output.getvalue().rstrip("\n")
        finally:
            sys.stdout = sys.__stdout__

        self.assertEqual(printed_result, "#")

    # Test for __str__ =============================
    def test_str(self):
        obj = Square(4, 6, 2, 1, 12)
        self.assertEqual(obj.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    # Test for update method==============
    def test_update_id(self):
        self.obj.update(id=89)
        self.assertEqual(self.obj.id, 89)

    def test_updata_width(self):
        self.obj.update(id=89, width=2)
        self.assertEqual(self.obj.width, 2)

    def test_update_height(self):
        self.obj.update(id=89, width=2, height=3)
        self.assertEqual(self.obj.height, 3)

    def test_update_x(self):
        self.obj.update(id=89, width=2, height=3, x=4)
        self.assertEqual(self.obj.x, 4)

    def test_update_y(self):
        self.obj.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(self.obj.y, 5)
"""


if __name__ == "__main__":
    unittest.main()
