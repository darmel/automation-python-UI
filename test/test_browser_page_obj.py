from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from duckduckgo_search_page import DuckDuckGoSearchPage
#from duckduckgo_search_page import DuckDuckGoSearchResultsPage



class TestBrowser():

    def test_duckduckgo_home_page(self, driver):
        search_page = DuckDuckGoSearchPage(driver) #search_page es la clase 
        search_page.open_page() #la clase ejecuta el metodo
        assert "DuckDuckGo" in (search_page.check_title())
        #title = search_page.check_title()
        #print(title)
        phrase = "casa"
        assert phrase in search_page.text_box(phrase) #comprueba el imput box
        time.sleep(1)

    def test_result_page(self, driver):
        search_page = DuckDuckGoSearchPage(driver)
        search_page.open_page()
        search_results_page = DuckDuckGoSearchPage(driver).search_phrase('panda')
        
        #comprueba caja de texto con la palabra buscada
        assert 'panda' in search_results_page.text_box('panda')  
        
        #comprueba los resultados
        assert all('panda' in title for title in search_results_page.get_all_results_tittles())
        
        #comprueba el titulo
        assert 'panda' in (search_results_page.check_title())

    def test_doble_search(self, driver):
        search_page = DuckDuckGoSearchPage(driver)
        search_page.open_page()
        palabra1 = 'dario'
        palabra2 = 'casa'
        search_results_page = search_page.search_phrase(palabra1)
        
        #comprueba el titulo para comprobar que esta en la pagina de resultados
        assert palabra1 in (search_results_page.check_title())

        # busca nueva palabra
        search_results_page = search_results_page.search_phrase(palabra2)

        #comprobar nuevos resultados
        assert all(palabra2 in title for title in search_results_page.get_all_results_tittles())

        


