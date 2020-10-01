
# Prerequisites
# You must have python 3 installed. It should come pre-installed on linux. If not, use:
# >brew install python3

# Or:
# >apt install python3

# For windows users, you can download python [Here](https://www.python.org/downloads/)
# (be sure to select "add python to system PATH" during the instillation, or else you will have to add it to the PATH manualy, which is a HUGE pain)

# You must also have the selenium module installed.
# This can be installed with command:
# >pip install selenium

# If you don't have pip installed, try:
# >brew install pip

# Or:
# >apt install pip

# This script uses chrome driver to produce a headless chrome environment. You must put the executable(chromedriver.exe) in you PATH for this script to work. You can download chromedriver.exe [Here](https://sites.google.com/a/chromium.org/chromedriver/downloads). 
# I recommend putting chromedriver.exe(or a copy of it) in the root directory of your python instillation, or if you're running Linux, put it in any bin directory of your distro(/bin should do nicley).

# Usage
# This script will ask you for a game pin upon startup. It will also ask you for a name and number of bots to join.
# Lets say you want your name to be "bot". Your name will be:
# >bot.(random number)




#A simple Kahoot bot that joins Kahoot game and sits idle
#Version 0.2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
#Asking for info here:
print("Liam's Kahoot spammer v 0.2")
pin = input("Please enter a game pin:")
name = input("Please enter a name:")
join = input("Please enter a amount of bots to join(Default is 50):")
tab = 0
nameb = str(name)
bot_num = 0
#Start chrome
print("Starting chrome...")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
#If join field is blank, then default is 50
if join=='':
    join=50
def namec():
    #Code for clarifying name
    global join, bot_num, nameb
    num=random.randint(1,999)*3
    if join=='1':
        nameb=name
        bot_num = bot_num + 1
    if int(join)>=2:
        if bot_num==join:
            print("Name generation completed")
        nameb=(name + '.' + str(num))
        bot_num = bot_num + 1
def bot():
    global nameb, driver, tab
    if bot_num==1:
        print("No new window necessary")
    elif bot_num >=2:
        print("Opening new window...")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[tab])
    print("Navigating to Kahoot...")
    #Navigate to kahoot.com
    driver.get("https://kahoot.it/")
    #Wait untill element is available
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'inputSession')))
    #Finding input box
    inputb = driver.find_element_by_id('inputSession')
    print("Joining game...")
    #Inputting pin
    inputb.send_keys(pin)
    inputb.submit()
    #Entering name
    element = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    gname = driver.find_element_by_id('username')
    namec()
    gname.send_keys(nameb)
    gname.submit()
    #Checking login
    print("Checking if login was succesfull...")
    try:
       content = driver.find_element_by_class_name('ng-binding') 
    except:
        print("Error checking page:\nId could have changed, or connection could have dropped.")
        x=input("Press any key to exit...")
    print("Success!")
    print("Bot [" + bot_num + "] is now in the game ;)")
    tab = tab + 1
#Code for running a set amount of times
for x in range(int(join)):
    bot()
