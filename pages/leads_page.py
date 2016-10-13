from base.base_page import BasePage
from base.locators import leads_locators


class LeadsPage(BasePage):

    def get_title(self):
        return self.get_element(leads_locators['title']).text

    def click_add_lead_button(self):
        self.get_element(leads_locators['add_lead_button']).click()

    def add_new_lead(self, **kwargs):
        for key in kwargs:
            locator = leads_locators.get(key, None)
            if locator:
                self.get_element(locator).send_keys(kwargs[key])
        self.get_element(leads_locators['save_button']).click()

    def get_lead_details_title(self):
        return self.get_element(leads_locators['lead_details_title']).text

    def get_lead_details_status(self):
        return self.get_element(leads_locators['lead_details_status']).text

    def navigate_to_lead_details(self, first_name, last_name):
        lead_name = "{} {}".format(first_name, last_name)
        lead_locator = leads_locators['smart_list_lead'][1].format(lead_name)
        self.get_element(leads_locators['smart_list_button']).click()
        self.get_element(('xpath', lead_locator)).click()

