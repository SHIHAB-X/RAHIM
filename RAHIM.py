import RAHIM
import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from RAHIM import RAHIM
 
        main_menu()
 
 
 
elif bit == "32bit":
 
        from RAHIM import RAHIM
 
 
        main_menu()
 
 
 
