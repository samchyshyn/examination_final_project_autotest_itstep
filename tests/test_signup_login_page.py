import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_logout
class TestSignupLoginLogautPage:

    def setup_method(self):
        hash_name = "%016x" % random.getrandbits(64)
        self.email_for_signup = f"{hash_name}@mail.com"
        self.password_for_signup = "Qa3654789"
        self.firstname_for_signup = "Gosha"
        self.lastname_for_signup = "Samrich"
        self.phone_for_signup = "0506547892"

    def test_get_main_page(self, browser):
            page = BasePage(browser, sets.PROD_SERVER)
            page.open()

    def test_signup_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_menu_signup()
        page.explicit_wait(2)
        page.is_h2_vhod()
        page.input_data_for_signup(self.firstname_for_signup, self.lastname_for_signup, self.email_for_signup,
                                   self.password_for_signup, self.phone_for_signup)
        page.explicit_wait(4)
        page.press_button_signup()
        page.is_alert_success()
        page.explicit_wait(3)

    def test_logout_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.press_button_logout()
        page.explicit_wait(3)
        page.is_menu_login()
        page.explicit_wait(3)

    def test_login_page(self, browser):
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


