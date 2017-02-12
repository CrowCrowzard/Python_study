# coding: UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, "html.parser")

    for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
        print (sibling)

if __name__ == '__main__':
    main()


