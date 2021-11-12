from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from duckduckgo_search_results import DuckDuckGoSearchResultsPage

search_input_locator = (By.ID, "search_form_input_homepage")

class DuckDuckGoSearchPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://duckduckgo.com/")
        
    def check_title(self):
        return self.driver.title

    def text_box(self, phrase):
        search_input = self.driver.find_element(*search_input_locator)
        search_input.send_keys(phrase)
        return(search_input.get_attribute('value'))
        

    def search_phrase(self, phrase):
        search_input = self.driver.find_element(*search_input_locator)
        search_input.clear()
        search_input.send_keys(phrase)
        search_input.send_keys(Keys.ENTER)
        return DuckDuckGoSearchResultsPage(self.driver)
