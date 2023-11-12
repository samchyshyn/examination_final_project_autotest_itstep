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

    #####################################################################################
    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_), \
            "Element LOGO_ not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.INPUT_SEARCH), \
            "Element INPUT_SEARCH not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SEARCH), \
            "Element BUTTON_SEARCH not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_kategory(self):
        assert self.is_element_present(*locators.BasePageLocators.MENU_KATEGORY), \
            "Element MENU_KATEGORY not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_menu_in_kategory_war_book(self):
        assert self.is_element_present(*locators.BasePageLocators.MENU_WAR_BOOK), \
            "Element MENU_WAR_BOOK not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_submenu_comiksy_marvel(self):
        assert self.hover_action(*locators.BasePageLocators.MENU_COMIKSY), \
            "The element MENU_COMIKSY is not present"
        assert self.is_element_present(*locators.BasePageLocators.SUB_MENU_COMIKSY_MARVEL), \
            "The element is SUB_MENU_COMIKSY_MARVEL not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    ##############################################################################################
    def is_info_block_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_NEW_PRODUCTS), \
            "Element SECTION_NEW_PRODUCTS not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_new_products_3(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_BOOK_3), \
            "Element NEW_BOOK_3 not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_pokazat_eshcho(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_POKAZAT_ESHCHO), \
            "Element BUTTON_POKAZAT_ESHCHO not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_hits_prodag(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_HITS_PRODAG), \
            "Element SECTION_HITS_PRODAG not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_bestseller_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_BESTSELLER_PRODUCTS), \
            "Element SECTION_BESTSELLER_PRODUCTS not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_prev_bestseller(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_BESTSELLER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_bestseller(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_BESTSELLER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_popular_authors(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_POPULAR_AUTHORS), \
            "Element SECTION_POPULAR_AUTHORS not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_popular_authors_3(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_AUTHOR_1), \
            "Element POPULAR_AUTHOR_1 not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_all_authors(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_ALL_AUTHORS), \
            "Element BUTTON_ALL_AUTHORS not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_popular_series(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_POPULAR_SERIES), \
            "Element SECTION_POPULAR_SERIES not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_popular_serija_3(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_SERIJA_3), \
            "Element POPULAR_SERIJA_3 not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_all_series(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_ALL_SERIES), \
            "Element BUTTON_ALL_SERIES not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_all_series(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_ALL_SERIES), \
            "Element SECTION_ALL_SERIES not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_war_books(self):
        assert self.is_element_present(*locators.MainPageLocators.MENU_WAR_BOOK), \
            "Element MENU_WAR_BOOK not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_sub_menu_history_of_wars(self):
        assert self.is_element_present(*locators.MainPageLocators.SUB_MENU_HISTORY_OF_WARS), \
            "Element SUB_MENU_HISTORY_OF_WAR not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
#####################################################################################################

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "Element SUBSCRIBE not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_avtors_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.AVTORS_FOOTER), \
            "Element AVTORS_FOOTER not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_war_book_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.WAR_BOOK_FOOTER), \
            "Element WAR_BOOK_FOOTER not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_osob_kabinet_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.OSOBYSTYJ_KABINET_FOOTER), \
            "Element OSOBYSTYJ_KABINET_FOOTER not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_koshyk_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.KOSHYK_FOOTER), \
            "Element KOSHYK_FOOTER not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")


