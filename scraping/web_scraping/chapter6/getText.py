# coding: UTF-8

from urllib.request import urlopen

def main():
    textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
    print (textPage.read())

if __name__ == '__main__':
    main()


