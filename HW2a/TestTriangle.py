import time
import unittest
from HtmlTestRunner.runner import HTMLTestRunner
from Bugfree_Triangle import classifyTriangle

class TestPruebaTest(unittest.TestCase):
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -1, -1),'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(202, 202, 0),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle("200",0, 0),'InvalidInput')
    
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(0,"200", 0),'InvalidInput')
    
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5, 2, 1),'Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(2, 5, 1),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,2, 5),'NotATriangle')
    
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral')
    
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(15,17,8),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(28,45,53),'Right')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(12,5, 13), 'Right')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(8, 6, 10), 'Right')
    
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(10, 15, 12),'Scalene')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 2),'Isoceles')
    
    def testIsocelesTriangleB(self):     
        self.assertEqual(classifyTriangle(4, 6, 6),'Isoceles')
    
    def testIsocelesTriangleC(self): 
        self.assertEqual(classifyTriangle(6, 4, 6),'Isoceles')
    
    def testIsocelesTriangleD(self): 
        self.assertEqual(classifyTriangle(6, 6, 4),'Isoceles')

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPruebaTest))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    runner = HTMLTestRunner(verbosity=2, output='report', report_name='report', open_in_browser=True, add_traceback=False)
    runner.run(suite)

if __name__ == "__main__":
    main()
    