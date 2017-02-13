# coding: UTF-8

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import sys

pages = set()
random.seed(datetime.datetime.now())

# ページで見つかったすべての内部リンクのリストを取り出す
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # "/"で始まるすべてのリンクを見つける
    for link in bsObj.findAll("a", 
            href=re.compile("^(\/|.*" + includeUrl + "|((?!.*pdf).)*$)")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks# - pages

# ページで見つかったすべての外部リンクのリストを取り出す
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 現在のURLを含まない"http"か"www"で始まるすべてのリンクを見つける
    for link in bsObj.findAll("a", 
            href=re.compile("^(http|www)((?!"+excludeUrl+").)*((?!.*pdf).)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                if link.attrs['href'] not in pages:
                    externalLinks.append(link.attrs['href'])

    return externalLinks

def getHtml(startingPage):
    try:
        html = urlopen(startingPage)
    except HTTPError as e:
        print (e)
        sys.exit()

    return html

def getRandomExternalLink(startingPage):
    html = getHtml(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print ("No external links, looking around the site for one")
        internalLinks = getInternalLinks(bsObj, startingPage)
        if len(internalLinks) == 0:
            print ("No link")
            sys.exit()

        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
        
def followExtenalOnly(startingSite):
    pages.add(startingSite)
    externalLink = getRandomExternalLink(startingSite)
    print ("Random external link is: " + externalLink)
    followExtenalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()

# サイトで見つかったすべての外部URLのリストを集める
def getAllExternalLinks(siteUrl):
    html = getHtml(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, siteUrl)
    externalLinks = getExternalLinks(bsObj, siteUrl)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print (link)

    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)
    
def main():
    url = "http://oreilly.com"
    #followExtenalOnly(url)
    allIntLinks.add(url)
    getAllExternalLinks(url)

if __name__ == '__main__':
    main()


