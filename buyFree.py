# Go through the checkout process for the items

import time
from selenium.webdriver.chrome.options import Options
from myBrowserOptions import launchDriver
import os
import sys

# -- Launch the browser -- 
driver = launchDriver(1)
url = str(sys.argv[1])
driver.get(url)

# Find the zero dollar option

# Click the checkout

# Pop up a visable window on this page to see payment process

# ? add a wait/"press enter to continue?"

# input adress details

# imput payment details

# finish Transaction - Pop this window up


driver.close()