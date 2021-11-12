from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement


SEARCH_TITLE_LBL = (By.XPATH, "//a[@class='result__a js-result-title-link']")
SEARCH_INPUT = (By.ID, "search_form_input")

class DuckDuckGoSearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_results_tittles(self):
        search_results = self.driver.find_elements(*SEARCH_TITLE_LBL)
        titles = [item.text.lower() for item in search_results]
        return titles

    def text_box(self, phrase): #comprueba caja de texto
        search_input = self.driver.find_element(*SEARCH_INPUT)
        return(search_input.get_attribute('value'))

    def check_title(self):
        return self.driver.title

    def search_phrase(self, phrase):
        search_input = self.driver.find_element(*SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase)
        search_input.send_keys(Keys.ENTER)
        return DuckDuckGoSearchResultsPage(self.driver)