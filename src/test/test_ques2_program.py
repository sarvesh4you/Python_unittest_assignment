'''
Created on 16-Sep-2018

@author: sarveshshrivastava
'''
import unittest, os, logging, sys
import HTMLTestRunner

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main.ques2_program import MyClass as my_cls

log = logging.getLogger("LogMessage: ")

csv_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data")
reports_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_reports")

csv_path = csv_dir + "\\sample_ips.csv"
corrupt_csv_path = csv_dir + "\\corrupt.csv"
no_file = csv_dir + "\\no_file.csv"


class TestQuestion2Program(unittest.TestCase):

    def test_01(self):
        self.assertEqual(my_cls.get_valid_ip_list(self, csv_path)[0], ['131.203.58.164', '161.9.97.102', '170.223.83.106'])
        log.debug("Test 1 : Passed")

    def test_02(self):
        self.assertEqual(my_cls.get_valid_ip_list(self, csv_path)[1], ['253.175.74.233', '14.198.213.117', '35.241.137.125'])
        log.debug("Test 2 : Passed")
        
    def test_03(self):
        self.assertEqual(my_cls.get_valid_ip_list(self, csv_path)[3], ['46.158.78.155', '66.171.220.230'])
        log.debug("Test 3 : Passed")
        
    def test_04(self):
        self.assertEqual(my_cls.get_valid_ip_list(self, csv_path)[5], ['9.42.42.0'])
        log.debug("Test 4 : Passed")
        
    def test_05(self):
        with self.assertRaises(FileNotFoundError):
            my_cls.get_valid_ip_list(self, no_file)
            
        log.debug("Test 5 : Passed")  
        
    def test_06(self):
        with self.assertRaises(UnicodeDecodeError):
            my_cls.get_valid_ip_list(self, corrupt_csv_path)
            
        log.debug("Test 6 : Passed")                   


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("LogMessage: ").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuestion2Program)
  
    outfile = open(reports_path + "\\TestReport_" + os.path.basename(__file__).split(".")[0] + ".html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report : GlobalLogic Python UnitTest Assignment',
                description='Testing \'get_valid_ip_list(csv file input)\' method'
                )
  
    runner.run(suite)
    outfile.close()
    
