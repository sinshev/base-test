from base import BasePage
from base.locators import header_locators


class Header(BasePage):

    def navigate_to_profile_settings(self):
        self.get_element(header_locators['user_info_icon']).click()
        self.get_element(header_locators['profile_settings']).click()

    def navigate_to_leads_page(self):
        self.get_element(header_locators['leads_icon']).click()
