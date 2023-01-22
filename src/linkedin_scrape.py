from bs4 import BeautifulSoup
import urllib
import requests
import time
import random
from dotenv import dotenv_values

config = dotenv_values(".env")


HOMEPAGE_URL = "https://linkedin.com/"
LOGIN_URL = "https://www.linkedin.com/uas/login-submit"
COOKIE_FILENAME = "./outputs/cookies.txt"
user_agents = [
  "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
  "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
  ]
random_user_agent = random.choice(user_agents)


class LinkedinScraper:

    def __init__(self):
        self.username = config['USER_EMAIL']
        self.password = config['USER_PASSWORD']

     
        self.session = requests.Session()
        self.session.headers.update(
            {'User-agent': random_user_agent,
            'Cookie':self.get_cookies('.linkedin.com')}
            )

    def login_to_linkedin(self):
        csrf = self.get_csrf_token()

        login_data = urllib.parse.urlencode({
            'session_key': self.username,
            'session_password': self.password,
            'loginCsrfParam': csrf,
        }).encode('utf8')

        self.load_page_using_requests(LOGIN_URL, login_data)
        return



    def get_csrf_token(self):
        page  = requests.get(HOMEPAGE_URL)
        soup = BeautifulSoup(page.text, features="html.parser")
        return soup.find('input', attrs={'name': 'loginCsrfParam'})['value']

    def get_cookies(self,domain):
        page  = requests.get(HOMEPAGE_URL)
        cookie_dict = page.cookies.get_dict(domain=domain)
        found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
        return ';'.join(found)

   

    def load_page_using_requests(self, url, data=None):
        try:
            if data is not None:
                response = self.session.post(url, data)
                
                self.save_html_to_file('post',response.content)
            else:
                response = self.session.get(url)
                self.save_html_to_file('get',response.content)
            return response.content
        except Exception as e:
            print(e)
            return 

    def save_html_to_file(self,filename, content):
        with open(f'./outputs/{filename}.html','w') as file:
                file.write(str(content))
        file.close()

    def retrieve_soup(self,url,data=None):
        html = self.load_page_using_requests(url, data)
        soup = BeautifulSoup(html, features = "html.parser")
        return soup

scraper = LinkedinScraper()

scraper.login_to_linkedin()

soup = scraper.retrieve_soup("https://www.linkedin.com/feed/")
print(soup.find("title"))

# soup = scraper.retrieve_soup("https://www.linkedin.com/search/results/people/?keywords=%22CTO%22%20AND%20%22Industrial%20Company%22%20AND%20%22Europe%22&origin=SWITCH_SEARCH_VERTICAL&sid=XhJ")
# with open('./outputs/soup.html','w') as file:
#     file.write(soup.prettify())
# file.close()
# # print(soup)




