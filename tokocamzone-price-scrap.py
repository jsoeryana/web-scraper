#These codes are written with Python 3

import bs4
import sys
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#change the URL below as necessary
target_url = "https://www.tokocamzone.com/kamera/Kamera-DSLR?limit=100"

#get the target page based on the above URL
uClient = requests.get(target_url, timeout=5)
print("opening ... " + uClient.request.url)

#store the html content into beatifulsoup object
page_soup = BeautifulSoup(uClient.content,"html.parser")
uClient.close()

#find all the html tags which contains the target data to parse
containers = page_soup.findAll("div",{"class":"caption"})

print("Item found = " + str(len(containers)))

#declare CSV file as output
out_filename = str(datetime.now()) + ".csv"
out_fileheader = "Article Name;Price\n"
csv_file = open(out_filename,"w")
csv_file.write(out_fileheader)

#parse and put the results into csv file
try:
    i = 1
    for container in containers:
        article_name = container.a.text
        article_price = container.findAll("p",{"class":"price"})
        csv_file.write(article_name + ";" + article_price[0].text.strip() + "\n")
        #print("\n" + str(i) +  " | " + article_name + " | " + article_price[0].text.strip())
        i += 1
    print("Output csv file separated by semicolon : " + csv_file.name)
except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    csv_file.close()
