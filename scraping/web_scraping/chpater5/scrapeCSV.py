# coding: UTF-8

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
    bsObj = BeautifulSoup(html, "html.parser")

    # 主たる比較表はページの最初の表
    table = bsObj.findAll("table",{"class":"wikitable"})[0]
    rows = table.findAll("tr")

    csvFile = open("../files/editors.csv", 'wt', newline='', encoding='UTF-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        csvFile.close()

if __name__ == '__main__':
    main()


