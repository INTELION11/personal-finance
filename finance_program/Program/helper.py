import os
import sys
import time as t

#def clear function
def clearr():
    os.system('cls' if os.name == 'nt' else 'clear')  

#def the processing function
def processing(text="Processing", duration=3, speed=0.5):
    end_time = t.time() + duration
    while t.time() < end_time:
        for dots in range(4):
            sys.stdout.write('\r' + text + '.' * dots + ' ' * (3 - dots))
            sys.stdout.flush() 
            t.sleep(speed)
    sys.stdout.write('\r' + ' ' * (len(text) + 3) + '\r')
    sys.stdout.flush()
    print(text)

#def the speed print function
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
