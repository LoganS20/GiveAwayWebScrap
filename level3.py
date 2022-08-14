# level3 - Check if the cost is zero, if so then start a buy function

import time
from selenium.webdriver.chrome.options import Options
from myBrowserOptions import launchDriver
import os
import sys

# -- Launch the browser -- 
driver = launchDriver(1)
url = str(sys.argv[1])
driver.get(url)

# Scrape the prices in different sizes

element = driver.find_element_by_id("MainContent")
print(element.text)



print (element)
# If zero then buy
if (False):

    # Check if there is a file to flag(.txt file) indicating not to buy on this website

    noFlag = False
    if(flag):
        #Make a flag

        noFlag = False  #----Can

    # start the buy sequence
    os.system('python buyFree.py '+ url)

    

driver.close()

