# coding: UTF-8

import csv
from urllib.request import urlopen
from io import StringIO

def main():
    data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv") \
            .read().decode('ascii', 'ignore')
    dataFile = StringIO(data)
    csvReader = csv.reader(dataFile)

    for row in csvReader:
        print (row)

if __name__ == '__main__':
    main()


