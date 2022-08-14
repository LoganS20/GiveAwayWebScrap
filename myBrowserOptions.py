from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# -- Config the browser options and launch driver --

def op1():
    option = Options()
    # run selenium in headless mode to save resources
    option.add_argument("--headless")
    # disable infobar showing chrome is being run by automated software
    option.add_argument("--disable-infobars")
    # block notifications in window, like those asking for location
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    # this will disable image loading
    option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    return option

# Same as Op1 but with a visable browser. Good for Debugging
def op2():
    option = Options()
    # disable infobar showing chrome is being run by automated software
    option.add_argument("--disable-infobars")
    # block notifications in window, like those asking for location
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

    return option

# Same as Op1 but allowing the url to see that we are running a headless browser
def op3():
    option = Options()
    # run selenium in headless mode to save resources
    option.add_argument("--headless")
    # block notifications in window, like those asking for location
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    # this will disable image loading
    option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    return option

def launchDriver(n):
    if n == 1: return webdriver.Chrome('chromedriver.exe', options=op1())
    if n == 2: return webdriver.Chrome('chromedriver.exe', options=op2())
    if n == 3: return webdriver.Chrome('chromedriver.exe', options=op3())
    else: exit("lanchDriver n error")
