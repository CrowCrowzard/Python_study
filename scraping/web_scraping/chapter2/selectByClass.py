# coding: UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html, "html.parser")

    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print (name.get_text())
    #nameList = bsObj.findAll(text="the prince")
    #print (len(nameList))

if __name__ == '__main__':
    main()

