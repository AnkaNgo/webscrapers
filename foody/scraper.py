# -*- coding: utf-8 -*-
import codecs
import sys

import sys
from encodingVienamese import convert 

import pandas as pd
import numpy as np
import string

from bs4 import BeautifulSoup
import urllib
import re
#from encodingVienamese  import no_accent_vietnamese
#!/usr/bin/python
# -*- coding: utf8 -*-


url = "https://www.foody.vn/ho-chi-minh/quan-an?CategoryGroup=food&c=quan-an&page=1"


import re
   

def scrape_1page(url):
    page_source = urllib.urlopen(url).read()
    soup = BeautifulSoup(page_source, "lxml")
    infor = get_name(soup)
    return infor
def get_name(soup):     
    namelist = []
    linklist = []
    resnames = soup.findAll('div',attrs = { 'class':'resname' })
    for items in resnames:
        name_atag = items.find('a',href = True)
        name = name_atag.text
        link = name_atag['href']
        foodylink = 'wwww.foody.vn'+link
        #print string.capwords(s.decode('utf8'))
        #name_us = string.capwords(name.decode('utf8'))
        vnname = convert(name)
        #print vnname
        namelist.append(vnname)
        linklist.append(foodylink)
        
    return namelist,linklist
def scrape_res_info(url2)
    res_page = urllib.urlopen(url).read()
    soup = BeautifulSoup(res_page,"lxml")
    
    return res_info
def get_menu(soup)
    
    return menu


inf = scrape_1page(url)
print inf