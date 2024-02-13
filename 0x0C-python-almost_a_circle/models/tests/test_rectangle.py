#!/usr/bin/python3
"""module contains test cases for the Rectangle class"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """tests for the rectangle class"""

    r3 = Rectangle(10, 2, 0, 0, 12)
    r4 = Rectangle(1, 2, 3, 4, "5")
    r5 = Rectangle(1, 2, 3, 4, 0)
    r6 = Rectangle(1, 2, 3, 4, -1)
    r7 = Rectangle(1, 2, 0, 4, 5)
    r8 = Rectangle(1, 2, 3, 0, 5)
    my_obj = Rectangle(1, 2, 3, 4, 5)
    obj = Rectangle(10, 10, 10, 10)  # iteration of id here..now 5

    def setUp(self):
        self.obj = Rectangle(1, 2, 3, 4, 5)

    def test_all_args(self):

        self.assertEqual(self.r3.id, 12)

    def test_id_as_string(self):

        self.assertEqual(self.r4.id, "5")

    def test_id_as_0(self):

        self.assertEqual(self.r5.id, 0)

    def test_id_as_neg(self):

        self.assertEqual(self.r6.id, -1)

    # Error handling for width
    def test_width_not_int(self):

        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4, 5)

    def test_neg_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4, 5)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4, 5)

    # Error handling cases for height ====================================

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4, 5)

    def test_neg_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 3, 4, 5)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4, 5)

    # Error handling cases for x ===============================

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3", 4, 5)

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4, 5)

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4", 5)

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4, 5)

    # Check for x and y values as 0 ===============================
    def test_x_zero(self):
        self.assertEqual(self.r7.x, 0)

    def test_y_zero(self):
        self.assertEqual(self.r8.y, 0)

    # Test for area ==========================
    def test_2_int(self):
        my_obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.my_obj.area(), 2)

    def test_neg_int(self):
        with self.assertRaises(ValueError):
            my_obj = Rectangle(-1, -2, 3, 4, 5)
            my_obj.area()

    def test_mixed_int(self):
        with self.assertRaises(ValueError):
            my_obj = Rectangle(-1, 2, 3, 4, 5)
            my_obj.area()

    def test_0_int(self):
        with self.assertRaises(ValueError):
            my_obj = Rectangle(0, 0, 3, 4, 5)
            my_obj.area()

    def test_strings(self):
        with self.assertRaises(TypeError):
            my_obj = Rectangle("1", "2", 3, 4, 5)
            my_obj.area()

    def test_float(self):
        with self.assertRaises(TypeError):
            my_obj = Rectangle(1.5, 2.5, 3, 4, 5)
            my_obj.area()

    # Test for display function========================
    """
    def test_display(self):
        my_obj = Rectangle(3, 2, 3, 4, 5)

        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            my_obj.display()
            printed_result = captured_output.getvalue().rstrip("\n")
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

        self.assertEqual(printed_result, "###\n###")
"""
    def test_display_1(self):
        my_obj = Rectangle(1, 1)

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
        obj = Rectangle(4, 6, 2, 1, 12)
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


if __name__ == "__main__":
    unittest.main()
