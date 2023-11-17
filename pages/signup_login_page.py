from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):

    def click_menu_signup(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.MENU_SIGNUP), \
            "The element MENU_SIGNUP is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h2_vhod(self):
        assert self.is_element_present(*locators.SignupPageLocators.H2_SIGNUP), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_data_for_signup(self, name, lastname, email, password, phone):
        assert self.input_data(*locators.SignupPageLocators.INPUT_NAME, name), \
            "The element INPUT_NAME is not present"
        assert self.input_data(*locators.SignupPageLocators.INPUT_LASTNAME, lastname), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupPageLocators.INPUT_EMAIL, email), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupPageLocators.INPUT_PHONE, phone), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupPageLocators.INPUT_CONFIRM_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_signup(self):
        assert self.click_element(*locators.SignupPageLocators.BUTTON_SIGNUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success(self):
        assert self.is_element_present(*locators.SignupPageLocators.ALERT_SUCCESS), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_menu_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.MENU_LOGIN), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_vhod(self):
        assert self.is_element_present(*locators.LoginPageLocators.H1_LOGIN), \
            "The element login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        
    def input_email_password(self, email, password):
        assert self.input_data(*locators.LoginPageLocators.INPUT_EMAIL, email), \
            "The element currency is not present"
        assert self.input_data(*locators.LoginPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_login(self):
        assert self.click_element(*locators.LoginPageLocators.BUTTON_LOGIN), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_logout_in_header(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_LOGOUT), \
            "Button MENU_LOGOUT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_logout(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.click_element(*locators.BasePageLocators.MENU_LOGOUT), \
            "Button MENU_LOGOUT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_menu_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_LOGIN), \
            "The element MENU_LOGIN is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

