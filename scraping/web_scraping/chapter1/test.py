# coding: UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print (bsObj.h1)

if __name__ == '__main__':
    main()


