from ..pages import base_page, locators
import inspect

class OrderPage(base_page.BasePage):

    # def click_on_logo(self):
    #     assert self.click_element(*locators.BasePageLocators.LOGO_), \
    #         "The element currency is not present or intractable"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The element is not present or intractable"
        price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
        price = int(price.replace(' грн / шт.')) # 1180
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")
    #    print(f" Ціна першого товару - {price}  ")
        if price:
            return price

    def add_to_cart_first_product1(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def press_btn_continue_shop_popup(self):
        assert self.click_element(*locators.OrderPageLocators.BTN_CONTINUE_SHOP_POPUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_to_cart_second_product(self):
        assert self.hover_action(*locators.OrderPageLocators.MENU_MAGAZINES), \
            "Element 'MENU_MAGAZINES' is not present"
        assert self.click_element(*locators.OrderPageLocators.SUB_MENU_MAGAZINE_UNIVERSE), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_alert_input_universe(self):
        assert self.is_element_present(*locators.OrderPageLocators.ALERT_MAGAZINE_UNIVERSE), \
            "The element ALERT_MAGAZINE_UNIVERSE is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_quantity_second_product(self):
        assert self.clear_field(*locators.OrderPageLocators.INPUT_QUANTITY), \
            "Element 'INPUT_QUANTITY' is not present"
        assert self.input_data(*locators.OrderPageLocators.INPUT_QUANTITY, 2), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def add_to_cart_second_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_SECOND_PRODUCT), \
            "The element BUTTON_ADD_SECOND_PRODUCT is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def input_search_3_product(self, searching):
        assert self.clear_field(*locators.BasePageLocators.INPUT_SEARCH), \
            "Element 'INPUT_QUANTITY' is not present"
        assert self.input_data(*locators.BasePageLocators.INPUT_SEARCH, searching), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def choice_is_searching_3_product(self):
        assert self.click_element(*locators.OrderPageLocators.MENU_IS_SEARCHING_1), \
            "The element MENU_IS_SEARCHING_1 is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def add_to_cart_3_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_3_PRODUCT), \
            "The element BUTTON_ADD_SECOND_PRODUCT is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def press_btn_view_your_cart(self):     ##################################################
        assert self.click_element(*locators.OrderPageLocators.BTN_VIEW_YOUR_CART), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_del_1_product_in_cart(self):
        assert self.click_element(*locators.OrderPageLocators.REMOVE_BTN_1_IN_CART), \
            "The element REMOVE_BTN_1_IN_CART is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_change_quantity_2_product(self):
        assert self.clear_field(*locators.OrderPageLocators.QUANTITY_SECOND_PRODUCT), \
            "Element 'INPUT_QUANTITY' is not present"
        assert self.input_data(*locators.OrderPageLocators.QUANTITY_SECOND_PRODUCT, 1), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_update_cart(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_UPDATE_CART), \
            "The element BUTTON_UPDATE_CART is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_CHECKOUT), \
            "The element BUTTON_CHECKOUT is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_alert_checkout(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.ALERT_ORDER_PLACEMENT, timeout=25), \
            "The element ALERT_ORDER_PLACEMENT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_press_button_post(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_POST), \
            "The element BUTTON_POST is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_city_search(self):
        assert self.click_element(*locators.OrderPageLocators.MENU_CITY_SEARCH), \
            "The element MENU_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def input_search_field_city(self, field_city):
        assert self.input_data(*locators.OrderPageLocators.FIELD_CITY_SEARCH, field_city), \
            "The element FIELD_CITY_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_city_result_search(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_RESULT_SEARCH), \
            "The element SELECT_RESULT_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_placeholder_search(self):
        assert self.click_element(*locators.OrderPageLocators.FIELD_PLACEHOLDER_SEARCH), \
            "The element FIELD_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_selected_placeholder(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_PLACEHOLDER_SEARCH), \
            "The element SELECT_PLACEHOLDER_SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_postpaid(self):
        assert self.click_element(*locators.OrderPageLocators.SELECT_BTN_POSTPAID), \
            "The element SELECT_BTN_POSTPAID is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

    def is_press_button_place_order(self):
        assert self.click_element(*locators.OrderPageLocators.BUTTON_PLACE_AN_ORDER), \
            "The element BUTTON_PLACE_AN_ORDER is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok ")

