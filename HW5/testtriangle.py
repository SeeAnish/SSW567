import unittest

from triangle import classifyTriangle

class TestTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classifyTriangle(2, 2, 2), "Equilateral triangle")
        #print("Test for Equilateral triangle passed")

    def test_right_angle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right angle triangle")
        #print("Test for Right angle triangle passed")

    def test_isosceles_triangle(self):
        self.assertEqual(classifyTriangle(4, 4, 5), "Isosceles triangle")
        #print("Test for Equilateral triangle passed")
    
    def test_scalene_triangle(self):
        self.assertEqual(classifyTriangle(10, 12, 15), "Scalene triangle")
        #print("Test for Scalene triangle passed")


if __name__ == "__main__":
    unittest.main(exit=False)