import bs4
import sys
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#change the URL below as necessary
target_url = "https://www.tokocamzone.com/kamera/Kamera-DSLR?limit=100"

uClient = requests.get(target_url, timeout=5)
print("opening ... " + uClient.request.url)
page_soup = BeautifulSoup(uClient.content,"html.parser")
uClient.close()

containers = page_soup.findAll("div",{"class":"caption"})

print("Item found = " + str(len(containers)))


out_filename = str(datetime.now()) + ".csv"
out_fileheader = "Article Name;Price\n"
csv_file = open(out_filename,"w")
csv_file.write(out_fileheader)

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