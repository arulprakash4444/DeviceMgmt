from os import system, name 
  
from time import sleep 
  
 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
# print out some text 
# print('hello geeks\n'*10) 
  
# sleep for 2 seconds after printing output 
# sleep(2) 
  
# now call function we defined above 
# clear() 