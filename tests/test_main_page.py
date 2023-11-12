import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_number_phone()
        page.is_button_telegram()
        page.is_button_registration()
        page.is_button_login()
        page.is_button_main_menu()
        page.is_button_oplata_dostavka()
        page.is_button_new_products()
        page.is_button_bestcellers()
        page.is_button_contacts()
        page.is_button_koshyk()
        page.is_search_input_field()
        page.is_search_button()
        page.is_element_logo()
        page.is_button_kategory()
        page.is_menu_in_kategory_war_book()
        page.is_submenu_comiksy_marvel()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_info_block_new_products()
        page.is_new_products_3()
        page.is_info_block_hits_prodag()
        page.is_button_prev_hits()
        # page.is_button_next_hits()
        page.is_info_block_bestseller_products()
        # page.is_button_prev_bestseller()
        page.is_button_next_bestseller()
        page.is_info_block_popular_authors()
        page.is_popular_authors_3()
        page.is_button_all_authors()
        page.is_info_block_popular_series()
        page.is_popular_serija_3()
        page.is_button_all_series()
        page.is_info_block_all_series()
        page.is_button_war_books()
        page.is_button_sub_menu_history_of_wars()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_button_avtors_footer()
        page.is_button_war_book_footer()
        page.is_button_osob_kabinet_footer()
        page.is_button_koshyk_footer()

    # def test_main_page_subscribe_action(self, browser):
    #     self.link_to_cabinet = browser.current_url
    #     page = MainPage(browser, self.link_to_cabinet)
    #     page.subscribe_action(self.email_for_subscribe)
    #     page.is_alert_success_after_subscribe()
