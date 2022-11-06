from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import pandas as pd
import os
import re
import random


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
        fn = open(file, "r",encoding="utf-8")
        for line in fn.read().splitlines():
            if line != "":
                numbers.append(line)
    elif re.search("message", file):
        fm = open(file, "r",encoding="utf-8")
        messages.append(quote(fm.read()))
fn.close()
fm.close()

count = 0
message_not_send = []
print(numbers)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s = Service('.\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
for column in numbers:
    message = messages[random.randint(0,len(messages)-1)]
    message = message.replace("\n","%0A")
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(column) + '&text=' + message
        sent = False
        sleep(random.randint(2,30))
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'p3_M1')))
            sleep(4)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon='send']/.."))).click()
            
            
            # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq'))).click()
            # wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-testid="send"]'))).click()
            print("successfully")
        except Exception as e:
            print("Sorry message could not sent to " + str(column))
            message_not_send.append(column)
        else:
            sent = True
            sleep(8)
            print('Message sent to: ' + str(numbers[count]))
        count = count + 1
    except Exception as e:
        print('Failed to send message to ' + str(numbers[count]) + str(e))
driver.quit()
print("The script executed successfully.")
df = pd.DataFrame(message_not_send,columns =['Numbers']) 
df.to_csv("Error_file.csv")
print("Error file created")