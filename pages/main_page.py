from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_registration(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_REGISTRATION), \
            "Button MENU_REGISTRATION is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_LOGIN), \
            "Button MENU_LOGIN is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wishlist(self):
        assert self.hover_action(*locators.BasePageLocators.ACCOUNT), \
            "Element 'Аккаунт' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MENU_WISHLIST), \
            "Button MENU_WISHLIST is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_number_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element number PHONE not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
