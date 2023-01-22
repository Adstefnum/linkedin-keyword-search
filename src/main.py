from tabulate import tabulate
from linkedin_scrape import LinkedinScraper
from linkedin_parser import LinkedinParser

#filters
scraper = LinkedinScraper()
scraper.login_to_linkedin()
soup = scraper.retrieve_soup("https://www.linkedin.com/search/results/people/?keywords=%22CTO%22%20AND%20%22Industrial%20Company%22%20AND%20%22Europe%22&origin=SWITCH_SEARCH_VERTICAL&sid=XhJ")

parser = LinkedinParser(soup)
results = parser.process_profile_lists()


print(tabulate(results, headers='firstrow', tablefmt='fancy_grid'))