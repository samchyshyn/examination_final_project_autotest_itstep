from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_number_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element number PHONE not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_telegram(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_TELEGRAM), \
            "Element BUTTON_TELEGRAM not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

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

    def is_button_main_menu(self):
        assert self.is_element_present(*locators.BasePageLocators.MAIN_MENU), \
            "Element MAIN_MENU not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_oplata_dostavka(self):
        assert self.is_element_present(*locators.BasePageLocators.OPLATA_I_DOSTAVKA_MENU), \
            "Element OPLATA_I_DOSTAVKA_MENU not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_new_products(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW_PRODUCTS_MENU), \
            "Element NEW_PRODUCTS_MENU not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_bestcellers(self):
        assert self.is_element_present(*locators.BasePageLocators.BESTCELLERY_MENU), \
            "Element BESTCELLERY_MENU not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS_MENU), \
            "Element CONTACTS_MENU not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_koshyk(self):
        assert self.is_element_present(*locators.BasePageLocators.KOSHYK), \
            "Element KOSHYK not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.INPUT_SEARCH), \
            "Element INPUT_SEARCH not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SEARCH), \
            "Element BUTTON_SEARCH not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")




