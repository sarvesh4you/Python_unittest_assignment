'''
Created on 15-Sep-2018

@author: sarveshshrivastava
'''
import unittest, os, logging, sys
import HTMLTestRunner

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main.ques1_program import MyClass as my_cls

log = logging.getLogger("LogMessage: ")

reports_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_reports")


class TestQuestion1Program(unittest.TestCase):

    def test_01(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "TestData", "Test"), "Given 'substr' is a prefix for 'mainstr'.")
        log.debug("Test 1 : Passed")

    def test_02(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "TestData", "Data"), "Given 'substr' is a suffix for 'mainstr'.")
        log.debug("Test 2 : Passed")
        
    def test_03(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "TestData", ""), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 3 : Passed")
        
    def test_04(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "", "Test"), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 4 : Passed")
        
    def test_05(self):
        self.assertEqual(my_cls.is_starts_or_ends_with(self, "", ""), "'mainstr' or/and 'substr' must not be empty.")
        log.debug("Test 5 : Passed")    
        
    def test_06(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, "TestData", 3)
        
        log.debug("Test 6 : Passed")
        
    def test_07(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, 3, "Data")
            
        log.debug("Test 7 : Passed")  
        
    def test_08(self):
        with self.assertRaises(TypeError):
            my_cls.is_starts_or_ends_with(self, 3, 3)
            
        log.debug("Test 8 : Passed")                   


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("LogMessage: ").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuestion1Program)
  
    outfile = open(reports_path + "\\TestReport_" + os.path.basename(__file__).split(".")[0] + ".html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report : Python UnitTest Demo',
                description='Testing \'is_starts_or_ends_with(mainstr, substr)\' method'
                )
  
    runner.run(suite)
    outfile.close()
    
