import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_menu_login()
        page.explicit_wait(3)
        page.is_h1_vhod()
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(3)
        page.press_button_login()
        page.is_button_logout_in_header()
        page.explicit_wait(3)

    def test_add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        global price_1_product
        global price_2_product
        global price_3_product
        price_1_product = page.add_to_cart_first_product()
        page.explicit_wait(3)
        page.press_btn_continue_shop_popup()
        page.explicit_wait(2)
        page.input_to_cart_second_product()
        page.is_alert_input_universe()
        page.explicit_wait(2)
        page.input_quantity_second_product()
        page.explicit_wait(3)
        price_2_product = page.add_to_cart_second_product()
        page.press_btn_continue_shop_popup()
        page.input_search_3_product(sets.SEARCHIN)
        page.explicit_wait(2)
        page.choice_is_searching_3_product()
        price_3_product = page.add_to_cart_3_product()
        page.explicit_wait(3)
        page.press_btn_view_your_cart()

    def test_in_cart_(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.check_total_price(price_1_product, price_2_product, price_3_product)
        page.explicit_wait(5)
        page.is_del_1_product_in_cart()
        page.is_change_quantity_2_product()
        page.explicit_wait(3)
        page.is_press_button_update_cart()
        page.explicit_wait(5)
        page.is_press_button_checkout()
        page.explicit_wait(15)

    def test_in_checkout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.is_press_button_post()
        page.is_press_city_search()
        page.input_search_field_city(sets.SEARCH_FIELD_CITY)
        page.explicit_wait(3)
        page.is_press_city_result_search()
        page.is_press_placeholder_search()
        page.explicit_wait(3)
        page.is_press_selected_placeholder()
        page.is_press_button_postpaid()
        page.explicit_wait(5)
        # page.is_press_button_place_order()
        # page.explicit_wait(10)

