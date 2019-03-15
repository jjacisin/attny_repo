import requests
from bs4 import BeautifulSoup
import re ##IMPORTS REGEX "regluar expression";


class BBScrapper:
    def webpage_html(self, url = 'http://www.bakerbotts.com/people/?letter=A&reload=false&scroll=0'):
        person_request = requests.get(url)
        self.person_html = person_request.text
        return self.person_html

    def listings_html(self, person_html = None):
        person_html = person_html or self.person_html #takes in a new html code or uses orginsl HTML
        person_soup = BeautifulSoup(person_html) #creates BeautifulSoup object
        attorney_soup =  person_soup.findAll('div', {'class':"person_result"})
        self.attorney_soup = attorney_soup
        return self.attorney_soup
