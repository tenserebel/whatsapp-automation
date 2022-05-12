import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import os
import re
import random
from urllib.parse import quote

files = []
directory = 'input_files'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        files.append(f)
print(files) 

numbers = []
messages = []
for file in files:
    if re.search("number", file):
        fn = open(file, "r")
        for line in fn.read().splitlines():
            if line != "":
                numbers.append(line)
    elif re.search("message", file):
        fm = open(file, "r")
        messages.append(fm.read())
fn.close()
fm.close()

for lead in numbers:
    message = messages[random.randint(0,len(messages)-1)]
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead)
    time.sleep(25)
    x3, y3 = [950,750] 
    pg.moveTo(x3, y3) 
    pg.click() 
    time.sleep(5) 
    pg.typewrite(message) 
    pg.press('enter')
    # width,height = pg.size()
    # pg.click(width/2,height/2)
    # time.sleep(8)
    # pg.hotkey('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')