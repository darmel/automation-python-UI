import json
import os
import pathlib
from distutils import util

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options



@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    #driver.maximize_window()
    yield driver
    driver.quit

'''
@pytest.fixture()
def config():
    #config_path = str(pathlib.Path(__file__).parent.absolute()) + '/config.json'
    with open(config_path) as config_file:
        config = json.load(config_file)

        assert config["browser"] in ['chrome', 'firefox', 'safari', 'edge']
        assert isinstance(config["implicitly_wait"], int)
        assert config["implicitly_wait"] > 0

        return config

@pytest.fixture()
def driver(config):
    headless = util.strtobool(os.environ.get('headless'))
    driver = None
    if config["browser"] == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    elif config["browser"] == 'firefox':
        options = Firefox_Options()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif config["browser"] == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    elif config["browser"] == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif config["browser"] == 'safari':
        driver = webdriver.Safari()

    driver.implicitly_wait(config["implicitly_wait"])
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='Ingresar ambiente sobre el que se quieren ejecutar las pruebas')
    parser.addoption('--headless', action='store', default='true', help='true para activar, false para desactivar')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["headless"] = config.getoption('headless')
'''