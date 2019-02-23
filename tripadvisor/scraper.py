import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import urllib
import re
## This scrapper get all the infor :name, adress, reviews of 1 url at 1st page

class scrape_infor (object):
    def __init__(self, url):
        self.url = url
        page_source = urllib.urlopen(self.url).read()
        self.soup = BeautifulSoup(page_source, "lxml")
     
        
    def get_info(self):
        soup = self.soup
        name = get_name(soup)
        rate = get_rating(soup)
        num = get_NumReviews(soup)
        adress = get_adress(soup)
        num_exl = get_exlReviews(soup)
        infor = [name,rate,num,adress,num_exl]
        return infor


class scrape_reviews(object):
    def __init__(self,soup):
        self.soup = soup
    def get_reviewsdate(self):
    #soup.findAll(id=re.compile("para$"))
    # <div class="hotels-review-list-parts-EventDate__event_date--1agCM"><span> October 2018</span></div>
        date_box_div = self.soup.findAll('div',attrs = {'class' :  "hotels-review-list-parts-EventDate__event_date--1agCM"})
        listdate = []
        for items in date_box_div:
            date_span = items.span
            dateofreview = date_span.text 
            items_date = dateofreview.split(':')[1]
            listdate.append(items_date)
        self.date = listdate
        return self.date
    def get_reviews_text(self):
    
        review_box = self.soup.findAll('q',attrs = {'class':"hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--1OjOL"})
        listreview = []
        for items in review_box:
            text_span = items.span
            text_review = text_span.text
            listreview.append(text_review)
        self.reviews = listreview
        return self.reviews
        
    def get_trip_type(self): 
    #<span class="trip_type_label">Trip type: </span>
        print "SOUP:"
        print self.soup
        triptype_box = self.soup.findAll('span', attrs = {'class' :"trip_type_label"})
        print triptype_box
        listtrip = ['hello']
        for items in triptype_box:
            text_span = items
            trip_text = text_span.text
            listtrip.append(trip_text)
        self.trip_type = listtrip
        return self.trip_type

def get_source(url):
    page_source = urllib.urlopen(url).read()
    soup = BeautifulSoup(page_source, "lxml")
    print "hello name"

    return soup
def get_name(soup):
    
    name_box = soup.find('h1', attrs={'class': 'ui_header h1'})
    name = name_box.text.strip()
    print "hello name"
    return name
 
def get_rating(soup):
    rate_box = soup.find('span',attrs = {'class':'hotels-hotel-review-about-with-photos-Reviews__overallRating--3cjYf'})
    rate = rate_box.text.strip()
    return rate
def get_NumReviews(soup):
    num_box = soup.find('span',attrs  = {'class':'hotels-hotel-review-about-with-photos-Reviews__seeAllReviews--3jEYF'})
    num = num_box.text.strip()

    return num
def get_adress(soup):
    adress_box = soup.find('span',attrs  = {'class':"public-business-listing-ContactInfo__nonWebLink--1EqMn"})
    adress = adress_box.text.strip()

    return adress
def get_exlReviews(soup):
    exl_box = soup.find('span',attrs = {'class':"hotels-hotel-review-community-content-review-list-parts-ReviewRatingFilter__row_num--4LVBi"})
    num_exl = exl_box.text.strip()
    return num_exl
   
def get_info(soup):
    name = get_name(soup)
    rate = get_rating(soup)
    num = get_NumReviews(soup)
    adress = get_adress(soup)
    num_exl = get_exlReviews(soup)
    infor = [name,rate,num,adress,num_exl]
    
    
    return infor    
    
    
    
    


 
def main():
    #TODO
    url = "https://www.tripadvisor.com.sg/Hotel_Review-g294265-d7056556-Reviews-Hotel_Jen_Orchardgateway_Singapore-Singapore.html"

    #soup = get_source(url)
    #infor = get_info(soup)
    #print infor
    newpage = scrape_infor(url)
    print newpage.get_info()
    reviews = scrape_reviews(newpage.soup)
    date = reviews.get_reviewsdate()
    reviews_text = reviews.get_reviews_text()
    trip = reviews.get_trip_type()
    print date
    print reviews_text
    print trip
if __name__ == "__main__":
    print ("get name, location, rating, number of reviews!")
    main()
    
 