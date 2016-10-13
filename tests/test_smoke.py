import pytest

from base.wrapper import SeleniumWrapper
from base import config, resources
from pages.login_page import LoginPage
from pages.header import Header
from pages.dashboard_page import DashboardPage
from pages.leads_page import LeadsPage
from pages.settings_page import SettingsMenu, LeadsSettingsPage
from utils.leads_api_calls import LeadsAPICalls


class TestBaseCRM(object):
    @classmethod
    def setup_class(cls):
        selenium_driver = SeleniumWrapper()
        cls.driver = selenium_driver.connect()
        cls.driver.implicitly_wait(10)
        cls.login_page = LoginPage(cls.driver)
        cls.header = Header(cls.driver)
        cls.dashboard = DashboardPage(cls.driver)
        cls.leads_page = LeadsPage(cls.driver)
        cls.settings_menu = SettingsMenu(cls.driver)
        cls.leads_settings = LeadsSettingsPage(cls.driver)
        cls.call = LeadsAPICalls()

    @classmethod
    def teardown_class(cls):
        cls.change_status_name(cls, current_status=resources.LEAD_CHANGED_STATUS,
                               new_status=resources.LEAD_INITIAL_STATUS)
        cls.delete_lead(cls, first_name=resources.LEAD_FIRST_NAME, last_name=resources.LEAD_LAST_NAME)
        cls.driver.quit()

    @pytest.fixture
    def login(self):
        assert self.login_page.get_title() == resources.LOGIN_PAGE_TITLE
        self.login_page.login_action(config.EMAIL, config.PASSWORD)

    def change_status_name(self, current_status, new_status):
        self.header.navigate_to_profile_settings()
        self.settings_menu.navigate_to_leads_settings()
        self.leads_settings.navigate_to_lead_statuses_settings()
        self.leads_settings.change_status_name(current_status=current_status, new_status=new_status)

    def add_lead(self, **kwargs):
        self.leads_page.click_add_lead_button()
        assert self.leads_page.get_title() == resources.NEW_LEAD_TITLE
        self.leads_page.add_new_lead(**kwargs)

    def delete_lead(self, first_name, last_name):
        lead_id = self.call.get_lead_id_by_full_name(first_name, last_name)
        self.call.delete_lead_by_id(id=lead_id)

    def test_smoke(self, login):
        assert self.dashboard.get_title() == resources.DASHBOARD_TITLE
        # Go to Leads page
        self.header.navigate_to_leads_page()
        assert self.leads_page.get_title() == resources.LEADS_TITLE
        # Add new Lead
        self.add_lead(first_name_field=resources.LEAD_FIRST_NAME,
                      last_name_field=resources.LEAD_LAST_NAME,
                      company_name_field=resources.LEAD_COMPANY_NAME)
        assert self.leads_page.get_lead_details_status() == resources.LEAD_INITIAL_STATUS
        # Change status
        self.change_status_name(current_status=resources.LEAD_INITIAL_STATUS, new_status=resources.LEAD_CHANGED_STATUS)
        assert self.leads_settings.check_status_presence(resources.LEAD_CHANGED_STATUS)
        # Check that status name change is reflected
        self.header.navigate_to_leads_page()
        self.leads_page.navigate_to_lead_details(resources.LEAD_FIRST_NAME, resources.LEAD_LAST_NAME)
        assert self.leads_page.get_lead_details_status() == resources.LEAD_CHANGED_STATUS
