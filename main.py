# Program to start the script at a set website at a set time

import os
import time


# Wait for a set time before starting
wait = "19:55" 
#while(time.strftime("%H:%M", time.localtime())!=wait): print("Waiting until "+wait); time.sleep(15); 

# Commented out the initial selection of pages in favor of the url array (bypass level1.py)
#url =  'https://contemporarykorowaidesigns.co.nz/collections?page=1'
#os.system('python level1.py '+url)


urls = [
    "https://contemporarykorowaidesigns.co.nz/collections/childrens-korowai",
    "https://contemporarykorowaidesigns.co.nz/collections/childrens-korowai?page=2",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Quarter-length",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Quarter-length?page=2",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Half-length",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Half-length?page=2",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Full-Length",
    "https://contemporarykorowaidesigns.co.nz/collections/adult-korowai/Full-Length?page=2"
]

end = "20:15"
while(time.strftime("%H:%M", time.localtime())!=end):
    for url in urls:
        os.system('python level2.py '+url)
    time.sleep(30)
    
    #subprocess.call(['python', 'level2.py', url])
    #threading.Thread(target=os.system(), args=(str('python level2.py ' + url)), daemon=True).start()
    #p = Popen([r'level2.py', url], shell=True, stdin=PIPE, stdout=PIPE)
    #output = p.communicate()

print()
print("    -- All urls launched from main.py")
print()