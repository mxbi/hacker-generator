import sys
from random import randint

complete = False

def validip():
    sub1 = randint(0,255)
    sub2 = randint(0,255)
    sub3 = randint(0,255)
    sub4 = randint(0,255)
    
    ip = str(sub1) + '.' + str(sub2) + '.' + str(sub3) + '.' + str(sub4)
    print(ip)
    
def invalidip():
    sub1 = randint(0,255)
    sub2 = randint(0,255)
    sub3 = randint(0,255)
    sub4 = randint(0,255)
    
    invalidsub = randint(1,4)
    if invalidsub == 1:
        sub1 = randint(256,399)
    elif invalidsub ==2:
        sub2 = randint(256,399)
    elif invalidsub == 3:
        sub3 = randint(256,399)
    else:
        sub4 = randint(256,399)
    
    ip = str(sub1) + '.' + str(sub2) + '.' + str(sub3) + '.' + str(sub4)
    print('hi')
    print(ip)
    
if len(sys.argv) == 1:
    print("Please specify either a 'valid' or 'invalid' IP address with this script")
else:
    if str(sys.argv[1]) == 'valid':
        validip()
        complete == True
    elif str(sys.argv[1]) == 'invalid':
        invalidip()
        complete == True
    elif complete == False:
        print("Please specify either a 'valid' or 'invalid' IP address with this script")
    
