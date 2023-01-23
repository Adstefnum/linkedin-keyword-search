from bs4 import BeautifulSoup
from lxml import etree

NAME_XPATH ='//div/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]' 
NAME_CLASS = 'app-aware-link '
ID_XPATH = '//*[@id="vOBumQanRr62leWLbm4DBA=="]/div/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a'#get the href and then split by / and then by ?
COMPANY_XPATH ='//*[@id="vOBumQanRr62leWLbm4DBA=="]/div/ul/li[3]/div/div/div[2]/div[1]/div[2]/div[1]/text()'
COMPANY_CLASS = 'entity-result__primary-subtitle t-14 t-black t-normal'
RESULTS_LIST_PATH = '//*[@id="M9H/vPChRKuQGMDaCVjs+Q=="]/div/ul'
RESULTS_CLASS = 'reusable-search__entity-result-list list-style-none'
INDIVIDUAL_RESULT_CLASS = 'reusable-search__result-container.entity-result.entity-result__item'

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

with open('./outputs/soup.html','r') as file:
    soup = file.read()
    beaut = BeautifulSoup(soup, features ='html.parser')
    results = beaut.find(class_=RESULTS_CLASS)
    names_and_ids = results.find_all(class_="entity-result__title-text t-16")
    print(names_and_ids)
    companies = results.find_all(class_="entity-result__primary-subtitle t-14 t-black t-normal")

    # parser = LinkedinParser(soup)
    # print(parser.get_value_of_text_element_using_xpath(NAME_XPATH))


