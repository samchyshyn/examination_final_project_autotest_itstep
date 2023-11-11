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



