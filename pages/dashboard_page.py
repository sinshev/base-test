from base import BasePage
from base.locators import dashboard_locators


class DashboardPage(BasePage):

    def get_title(self):
        return self.get_element(dashboard_locators['title']).text
