from selenium.common.exceptions import TimeoutException

from base import BasePage
from base.locators import settings_locators


class SettingsMenu(BasePage):

    menu_locators = settings_locators['menu']

    def navigate_to_manage_accounts_settings(self):
        self.get_element(self.menu_locators['manage_accounts']).click()

    def navigate_to_manage_users_settings(self):
        self.get_element(self.menu_locators['manage_users']).click()

    def navigate_to_profile_settings(self):
        self.get_element(self.menu_locators['profile']).click()

    def navigate_to_leads_settings(self):
        self.get_element(self.menu_locators['leads']).click()


class LeadsSettingsPage(BasePage):

    leads_locators = settings_locators['leads']

    def get_title(self):
        return self.get_element(self.leads_locators['title']).text

    def navigate_to_lead_statuses_settings(self):
        self.get_element(self.leads_locators['lead_statuses']['tab']).click()

    def check_status_presence(self, status_name):
        status_locator = self.leads_locators['lead_statuses']['status'][1].format(status_name)
        try:
            self.get_element(("xpath", status_locator))
            return True
        except TimeoutException:
            return False

    def change_status_name(self, current_status, new_status):
        edit_button_locator = self.leads_locators['lead_statuses']['edit_status_button'][1].format(current_status)
        self.get_element(("xpath", edit_button_locator)).click()
        status_name_field_locator = self.leads_locators['lead_statuses']['status_name_field'][1].format(current_status)
        status_name_field = self.get_element(("xpath", status_name_field_locator))
        status_name_field.clear()
        status_name_field.send_keys(new_status)
        self.get_element(self.leads_locators['lead_statuses']['save_button']).click()