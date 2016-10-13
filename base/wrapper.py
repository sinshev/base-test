import os
from selenium import webdriver
from pyvirtualdisplay import Display


from .config import LOGIN_URL, ENV


class SeleniumWrapper(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton Pattern"""
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, host=LOGIN_URL):
        if ENV == 'jenkins':
            display = Display(visible=0, size=(1366, 768))
            display.start()
        self.driver = webdriver.Chrome(os.path.dirname(__file__) + '/../utils/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(host)
        return self.driver