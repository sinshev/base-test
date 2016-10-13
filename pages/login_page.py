from base import BasePage, locators


class LoginPage(BasePage):

    def get_title(self):
        return self.get_element(locators.login_locators['title']).text

    def login_action(self, username, password):
        email_field_element = self.get_element(locators.login_locators['email_field'])
        password_field_element = self.get_element(locators.login_locators['password_field'])
        login_button = self.get_element(locators.login_locators['login_button'])
        email_field_element.send_keys(username)
        password_field_element.send_keys(password)
        login_button.click()