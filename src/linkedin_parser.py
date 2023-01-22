from bs4 import BeautifulSoup
from lxml import etree

NAME_XPATH ='//*[@id="vOBumQanRr62leWLbm4DBA=="]/div/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]/text()' 
ID_XPATH = '//*[@id="vOBumQanRr62leWLbm4DBA=="]/div/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a'#get the href and then split by / and then by ?
COMPANY_XPATH ='//*[@id="vOBumQanRr62leWLbm4DBA=="]/div/ul/li[3]/div/div/div[2]/div[1]/div[2]/div[1]/text()'
RESULTS_LIST_PATH = ''

class LinkedinParser:

    def __init__(self, soup):
        self.document_object_model = etree.HTML(str(soup))
        self.results = [['ID','Name','Company']]

    def get_value_of_text_element_using_xpath(self,path):
        return self.document_object_model.xpath(f'{path}')[0].text

    def get_value_of_link_element(self,path):
        pass

    def get_all_profile_lists(self,path):
        pass

    def process_profile_lists(self):
        profiles_html = get_all_profile_lists()

        #find all profiles in the list, there should be a wrapper for each
        #find all those wrappers
        
        #in each of those wrappers, find the name, ID, company
        #append to the results list as a [ID, Name, Company]



