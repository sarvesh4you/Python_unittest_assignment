'''
Created on 16-Sep-2018

@author: sarveshshrivastava
'''
import csv,os,sys
import re
from copy import deepcopy
class MyClass(object):
   
    def __init__(self):
        '''
        Constructor
        '''
        
    def get_valid_ip_list(self, csv_file_path):
       
        final_rows = []
        pat = re.compile(r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])")
        try:
            with open(csv_file_path, 'r') as csvfile: 
   
                csvreader = csv.reader(csvfile, delimiter=',')  
               
                for row in csvreader:
                    temp = deepcopy(row)
                    for col in row:
                        if col.startswith("127") or col.startswith("192") or col.startswith("169") or not pat.match(col):
                            temp.remove(col)
       
                    final_rows.append(temp)
                csvfile.close()
                del temp
                del csvreader
    
            return final_rows

        except FileNotFoundError as e:
            raise e
         
        except IOError as e:
            raise e
              
        except UnicodeDecodeError as e:
            raise e  
        
        except Exception as e:
            raise e
if __name__ == "__main__":
    
    obj = MyClass()
    print(os.path.basename(__file__).split(".")[0])
    #print(obj.get_valid_ip_list("sample_ips.csv"))
    
