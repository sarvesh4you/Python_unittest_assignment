'''
Created on 15-Sep-2018

@author: sarveshshrivastava
'''
import unittest
import logging
import sys,os

sys.path.append("D:\\sarveshshrivastava\\workspace\\Python_Assignment\\src")
from main.ques1_program import MyClass as my_cls
import HTMLTestRunner

log = logging.getLogger("LogMessage: ")
reports_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_reports")


class TestQuestion1Program(unittest.TestCase):

    def test_01(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "GlobalLogic", "Global"), "Given 'substr' is a prefix for 'mainstr'.")
        log.debug("Test 1 : Passed")

    def test_02(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "GlobalLogic", "Logic"), "Given 'substr' is a suffix for 'mainstr'.")
        log.debug("Test 2 : Passed")
        
    def test_03(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "GlobalLogic", ""), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 3 : Passed")
        
    def test_04(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "", "Global"), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 4 : Passed")
        
    def test_05(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "", ""), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 5 : Passed")    
        
    def test_06(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, "GlobalLogic", 3)
        
        log.debug("Test 6 : Passed")
        
    def test_07(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, 3, "Logic")
            
        log.debug("Test 7 : Passed")  
        
    def test_08(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, 3, 3)
            
        log.debug("Test 8 : Passed")                   


if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "LogMessage: " ).setLevel( logging.DEBUG )
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuestion1Program)
  
    outfile = open(reports_path+"\\TestReport_"+os.path.basename(__file__).split(".")[0]+".html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report : GlobalLogic Python UnitTest Assignment',
                description='Testing \'is_starts_or_ends_with(mainstr, substr)\' method'
                )
  
    runner.run(suite)
    outfile.close()
    
