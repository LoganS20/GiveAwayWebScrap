# Level1 - First approach to the website. Opens further windows on each product to begin the search. --NA

from selenium.webdriver.chrome.options import Options
from myBrowserOptions import launchDriver
import os
import sys

# -- Launch the browser -- 
driver = launchDriver(1)
url = str(sys.argv[1])
driver.get(url)

# If there is another page of options then launch this script there too 
if (False):
    url2 = 'https://contemporarykorowaidesigns.co.nz/collections?page=2'
    #url2 = USE HREF FROM PAGE
    os.system('python level1.py ' + url2)

# Find the product catagories on this page and 
pageCatagories = []

# launch new windows on those catagories
for catagory in pageCatagories:
    os.system('python level2.py ' + catagory)

# Close after all catagories have been opened
driver.close()



