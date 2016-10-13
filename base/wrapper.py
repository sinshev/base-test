import os
from selenium import webdriver

from .config import LOGIN_URL


class SeleniumWrapper(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton Pattern"""
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, host=LOGIN_URL):
        self.driver = webdriver.Chrome(os.path.dirname(__file__) + '/../utils/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(host)
        return self.driver