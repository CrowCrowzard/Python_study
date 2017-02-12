# coding: UTF-8

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def main():
    try:
        html = urlopen("https://pythonscrapingthisurldosnotexist.com")
    except HTTPError as e:
        print (e)
    except URLError as e:
        print ("The server could not be found!")
    else:
        print ("It Worked!")

if __name__ == '__main__':
    main()


