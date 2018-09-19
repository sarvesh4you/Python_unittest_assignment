'''
Created on 15-Sep-2018

@author: sarveshshrivastava
'''
class MyClass(object):
  
    def __init__(self):
        '''
        Constructor
        '''
        
    def is_starts_or_ends_with(self, mainstr, substr): 
        
        try: 
            
            if type(mainstr) is str and type(substr) is str:
                
                if mainstr and substr:
                    if mainstr.startswith(substr):
                        return "Given 'substr' is a prefix for 'mainstr'."
                
                    elif mainstr.endswith(substr):
                        return "Given 'substr' is a suffix for 'mainstr'."
        
                    else:
                        return "Given 'substr' is not a prefix or suffix for 'mainstr'."
    
                else:
                    return "'mainstr' or/and 'substr' must not be empty."
            
            else:
            
                raise TypeError("Type of 'mainstr' or/and 'substr' must be a String only.")
        
        
        except Exception as e:
            raise e
        
