# level2 - Scape the items off the catagory page and launch level3 on each item. Repeat until timed out.

import sys
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
URL = str(sys.argv[1])
page = requests.get(url=URL, headers=headers)

# Scrape the item links from the page
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('a', class_="grid-product__link")

pageItems = []
for result in results:
    pageItems.append(str("https://contemporarykorowaidesigns.co.nz" + result.get('href')))

# Open level3 on each item
for item in pageItems:
    #os.system('python level3.py ' + item)
    print("Opening: "+item)



# -- Launch the browser -- 
#driver = launchDriver(1)
#url = str(sys.argv[1])
#driver.get(url)

# Check if the catagory page is empty of items --NA
# Check if there is another page of items, if so then open another shell on that page --NA

# End if the time goes out to 20:15. Someone else has already won.
#end = "20:15"
#while(time.strftime("%H:%M", time.localtime())!=end):
    




