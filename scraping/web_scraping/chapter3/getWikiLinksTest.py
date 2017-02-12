# coding: UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
    bsObj = BeautifulSoup(html, 'html.parser')

    for link in bsObj.findAll('a'):
        if 'href' in link.attrs:
            print (link.attrs['href'])

if __name__ == '__main__':
    main()


