from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return str(self.driver.current_url)

    def get_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def hover_over_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def click_on_element(self, element):
        element.click()