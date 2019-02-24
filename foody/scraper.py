import pandas as pd
import numpy as np
import string

from bs4 import BeautifulSoup
import urllib
import re

url = "https://www.foody.vn/ho-chi-minh/quan-an?CategoryGroup=food&c=quan-an&page=1"
def scrape_1page(url):
    page_source = urllib.urlopen(url).read()
    soup = BeautifulSoup(page_source, "lxml")
    infor = get_name(soup)
    return infor
def get_name(soup):
     
    namelist = []
 
    resnames = soup.findAll('div',attrs = { 'class':'resname' })
    for items in resnames:
        name_atag = items.find('a',href = True)
        name = name_atag.text
        #print string.capwords(s.decode('utf8'))
        name_us = string.capwords(name.decode('utf8'))

        namelist.append(name_us)
     
    return namelist

inf = scrape_1page(url)
print len(inf)