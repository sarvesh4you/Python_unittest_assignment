# Python_unittest_assignment

#### System Requirement:

* Python 3.
* Any IDE i.e. PyDev, PyCharm (optional).

#### Framework and Package Structure:
  -Unittest Based Framework
  
  ***It comprises two main folders:-***
  1) main
  2) test
  
  
1)***Python_unittest_assignment\src\main*** contains 2 modules.
  ``` ques1_program.py ``` 
  ``` ques2_program.py ```   
  ***These modules contain the source code of the problems.***  
  
2)***Python_unittest_assignment\src\test*** contains 3 modules and 2 folders.
  ``` test_ques1_program.py ``` 
  ***Contains unit tests for 'ques1_program.py module'.*** 
  
  ``` test_ques2_program.py ```  
  ***Contains unit tests for 'ques2_program.py module'.***
  
  ``` HTMLTestRunner.py ```
  ***Contains code for generating clear HTML reports after executing unit tests.***
  
  ``` test_reports ```
  ***Contains HTML test reports generated through HTMLTestRunner.py.***
  
  ``` test_data ``` 
  ***Contains any test data if required.***  
  
  

#### Execution Steps:
***Please follow the instructions to execute the tests on local:***

1. By Using cmd/terminal:
   - To Execute through unittest (It will not generator the html test reports under 'test_reports' folder)
	```(after navigating to the test module) python -m unittest test_ques1_program.py```
	
   - To Execute through HTMLTestRunner (It will generator the html test reports under 'test_reports' folder)
    ``` (after navigating to the test module) python test_ques1_program.py``` 

	
2. By Using IDE i.e. PyDev:
   - To Execute through unittest (It will not generator the html test reports under 'test_reports' folder)
	``` Run As Python unit-test```
	
   - To Execute through HTMLTestRunner (It will generator the html test reports under 'test_reports' folder)
    ``` Run As Python Run``` 


#### Problem Statements:	

***ques1_program.py*** 
```
Ques1 :  WAP to check if the substr is the prefix or suffix for the given string
    def is_starts_or_ends_with(str,substr):
        “”Function to check if the substr is the prefix or suffix for the given string“”
```

***ques2_program.py*** 
```
Ques2:  WAP to parse large CSV file consisting of multiple IPs in every row.We have to remove Invalid IPs from each and every row.
Create below function inside a class.

def get_valid_ip_list(csv file input):

            “”Function to parse the given csv file and removes the Invalid IP from each row 

               and print  each row with valid ips.””

Write regex to see if the IP is valid or not.Also remove Private IPs that starts with 192.x.x.x, 169.x.x.x and local host ip 127.x.x.x.

You can use sample file with rows like : 172.3.4.5 , 192.2.4.5, " "
```
