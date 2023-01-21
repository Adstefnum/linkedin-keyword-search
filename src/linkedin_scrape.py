import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import urllib
import requests
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

filters = []

# response = requests.get("https://www.linkedin.com/search/results/people/?keywords=%22CTO%22%20AND%20%22Industrial%20Company%22%20AND%20%22Europe%22&origin=SWITCH_SEARCH_VERTICAL&sid=XhJ"


cookies_filename = "./outputs/cookies.txt"

class LinkedinScraper:

    def __init__(self):
        self.username = config['USER_EMAIL']
        self.password = config['USER_PASSWORD']

           # Simulate browser with cookies enabled
        self.cookies = cookielib.MozillaCookieJar(cookies_filename)
        if os.access(cookies_filename, os.F_OK):
            self.cookies.load()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler(),
            urllib.request.HTTPHandler(debuglevel=0),
            urllib.request.HTTPSHandler(debuglevel=0),
            urllib.request.HTTPCookieProcessor(self.cookies)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'))
        ]
       

    def login_to_linkedin(self):
        csrf = self.get_csrf_token()

        login_data = urllib.parse.urlencode({
            'session_key': self.username,
            'session_password': self.password,
            'loginCsrfParam': csrf,
        }).encode('utf8')

        self.load_page("https://www.linkedin.com/uas/login-submit", login_data)
        self.cookies.save()

        return


    def get_csrf_token(self):
        page  = requests.get("https://linkedin.com/")
        soup = BeautifulSoup(page.text, features="html.parser")
        return soup.find('input', attrs={'name': 'loginCsrfParam'})['value']

    #sleep after each tries, receive max_tries as arg
    def load_page(self, url, data=None):

        try:
            if data is not None:
                response = self.opener.open(url, data)
            else:
                response = self.opener.open(url)
            return ''.join([str(l) for l in response.readlines()])
        except Exception as e:
            return self.load_page(url, data)

    def retrieve_soup(self,url,data=None):
        html = self.load_page(url, data)
        soup = BeautifulSoup(html, "html.parser")
        return soup

scraper = LinkedinScraper()

scraper.login_to_linkedin()

# soup = scraper.retrieve_soup("https://www.linkedin.com/feed/")
# print(soup.find("title"))

soup = scraper.retrieve_soup("https://www.linkedin.com/search/results/people/?keywords=%22CTO%22%20AND%20%22Industrial%20Company%22%20AND%20%22Europe%22&origin=SWITCH_SEARCH_VERTICAL&sid=XhJ")
with open('./outputs/soup.html','w') as file:
    file.write(soup.prettify())
file.close()
# print(soup)




