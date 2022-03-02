from pynput.keyboard import Key, Controller
import time 
import json
import random

fcrd = json.load(open(r"tspd.json", 'r'))

password = ''.join([str(random.randrange(10)) for x in range(4)])
fcrd['Screen Time'] = password

def countdown(t=5):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Strating!')

countdown()



keyboard = Controller()

def presser(l):
    for key in l:
        keyboard.press(key)
        keyboard.release(key)

presser(password)
time.sleep(1)
presser(password)
try:
    json.dump(fcrd, open(r"tspd.json", 'w'))
except Exception as e:
    print(password)
    print(e)

input()
