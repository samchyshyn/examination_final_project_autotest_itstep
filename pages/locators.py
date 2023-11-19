from selenium.webdriver.common.by import By


class BasePageLocators:
    PHONE = (By.XPATH, '//span[text()="+38 073 938 79 43"]')
    BUTTON_TELEGRAM = (By.XPATH, '//a[@class="social-logo telegram"]')
    ACCOUNT = (By.XPATH, '//div[@class="header-links-wrapper"]')
    MENU_SIGNUP = (By.XPATH, '//a[@class="ico-register"]')
    MENU_LOGIN = (By.XPATH, '//a[@class="ico-login"]')
    MENU_WISHLIST = (By.XPATH, '//a[@class="ico-wishlist"]')
    MENU_LOGOUT = (By.XPATH, '//a[@class="ico-logout"]')

    LOGO_ = (By.XPATH, '//a[@class="logo"]')
    MAIN_MENU = (By.XPATH, '//a[text()="Головна"]')
    OPLATA_I_DOSTAVKA_MENU = (By.XPATH, '//ul[@class="top-menu"]//a[@href="/ua/oplata-i-dostavka"]')
    NEW_PRODUCTS_MENU = (By.XPATH, '//a[@href="/ua/newproducts"]')
    BESTCELLERY_MENU = (By.XPATH, '//ul[@class="top-menu"]//a[@href="/ua/newproducts"]')
    CONTACTS_MENU = (By.XPATH, '//a[@href="/ua/contactus"]')
    KOSHYK = (By.XPATH, '//a[@class="cart-trigger"]')
    INPUT_SEARCH = (By.XPATH, '//input[@id="small-searchterms"]')
    BUTTON_SEARCH = (By.XPATH, '//button[@type="submit"]')
    MENU_KATEGORY = (By.XPATH, '//span[@class="category-navigation-title"]')
    MENU_HUDOJNJA_LITERATURA = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Художня література"]')
    MENU_WAR_BOOK = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Військова книга"]')
    MENU_COMIKSY = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Комікси"]')
    SUB_MENU_COMIKSY_MARVEL = (By.XPATH, '//div[@class="two-columns-area-left"]//li[7]//a[text()="Комікси Marvel"]')
    BUTTON_GOTOTOP = (By.XPATH, '//div[@id="goToTop"]')
    ####################################################################
    SUBSCRIBE = (By.XPATH, "//button[text() = 'Підписатися']")
    INPUT_SUBSCRIBE = (By.XPATH, '//input[@class="newsletter-subscribe-text"]')
    ALERT_SUCCESS = (By.XPATH, '//div[contains(text(), "Дякуємо")]')
    ALERT_ERROR = (By.XPATH, "//div[@id = 'alert-error']")

    OPLATA_I_DOSTAVKA_FOOTER = (By.XPATH, '//div[@class="footer-block"]//a[text()="Оплата і доставка"]')
    AVTORS_FOOTER = (By.XPATH, '//a[text()="Автори"]')
    WAR_BOOK_FOOTER = (By.XPATH, '//div[@class="footer-block"]//a[text()="Військова книга"]')
    OSOBYSTYJ_KABINET_FOOTER = (By.XPATH, '//a[text()="Особистий кабінет"]')
    KOSHYK_FOOTER = (By.XPATH, '//a[text()="Кошик"]')

class MainPageLocators:
    # SECTION_NEW_PRODUCTS = (By.XPATH, '//div[@class="page home-page"]/div/div[1]/div[@class="item-grid"]')
    SECTION_NEW_PRODUCTS = (By.XPATH, '//div[@class="product-grid"][1]')
    NEW_BOOK_3 = (By.XPATH, '//div[@class="product-grid"][1]//div[@class="item-box"][3]')
    BUTTON_POKAZAT_ESHCHO = (By.XPATH, '//a[text()="Показать еще"]')
    SECTION_HITS_PRODAG = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][1]')
    # SECTION_HITS_PRODAG = (By.XPATH, '//div[@id="jcarousel-3-488"]')
    BUTTON_PREV_HITS = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][1]//button[@aria-label="Previous"]')
    BUTTON_NEXT_HITS = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][1]//button[@aria-label="Next"]')
    SECTION_BESTSELLER_PRODUCTS = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][2]')
    BUTTON_PREV_BESTSELLER = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][2]//button[@aria-label="Previous"]')
    BUTTON_NEXT_BESTSELLER = (By.XPATH, '//div[@class="page-body"]//div[@class="jCarouselMainWrapper"][2]//button[@aria-label="Next"]')
    SECTION_POPULAR_AUTHORS = (By.XPATH, '//div[@class="product-grid"][2]')
    POPULAR_AUTHOR_1 = (By.XPATH, '//div[@class="product-grid"][2]//div[@class="item-box"][1]')
    BUTTON_ALL_AUTHORS = (By.XPATH, '//a[text()="Все авторы"]')

    SECTION_POPULAR_SERIES = (By.XPATH, '//div[@class="product-grid"][3]')
    POPULAR_SERIJA_3 = (By.XPATH, '//div[@class="product-grid"][3]//div[@class="item-box"][3]')
    BUTTON_ALL_SERIES = (By.XPATH, '//a[text()="Все серии"]')
    SECTION_ALL_SERIES = (By.XPATH, '//div[@class="category-grid home-page-category-grid"]')

    MENU_HUDOJNJA_LITERATURA = (By.XPATH, '//a[text()=" Художня література "]')
    MENU_WAR_BOOK = (By.XPATH, '//a[text()=" Військова книга "]')

class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, '//div[@class="product-grid"][1]//div[@class="item-box"][3]')
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, '//div[@class="product-grid"][1]//div[@class="item-box"][8]//span[text() ="У кошик"]')
    PRICE_FIRST_PRODUCT = (By.XPATH, '//strong[@class="price"]')

    BTN_CONTINUE_SHOP_POPUP = (By.XPATH, '//a[text()="Продовжити покупки"]')
    BTN_VIEW_YOUR_CART = (By.XPATH, '//a[text() = "Подивитися ваш кошик"]')

    MENU_MAGAZINES = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Журнали"]')
    SUB_MENU_MAGAZINE_UNIVERSE = (By.XPATH, '//div[@class="two-columns-area-left"]//li[4]//a[text()="Всесвіт"]')
    ALERT_MAGAZINE_UNIVERSE = (By.XPATH, '//h1[text()="Журнал Всесвіт"]')
    INPUT_QUANTITY = (By.XPATH, '//input[@class="productQuantityTextBox"]')
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, '//span[text() ="У кошик"]')
    MENU_IS_SEARCHING_1 = (By.XPATH, '//li[@class="ui-menu-item"][1]')
    BUTTON_ADD_3_PRODUCT = (By.XPATH, '//button[@class="button-1 add-to-cart-button nopAjaxCartProductVariantAddToCartButton"]')

    REMOVE_BTN_1_IN_CART = (By.XPATH, '//tr[1]//button[@class="remove-btn"]')
    QUANTITY_SECOND_PRODUCT = (By.XPATH, '//tr[1]//input[@class="qty-input"]')
    BUTTON_CHECKOUT = (By.XPATH, '//button[@name="checkout"]')
    BUTTON_UPDATE_CART = (By.XPATH, '//button[text()="Оновити кошик"]')

    ALERT_ORDER_PLACEMENT = (By.XPATH, '//div[@class="page-title"]')    #   ОФОРМЛЕННЯ ЗАМОВЛЕННЯ
    BUTTON_POST = (By.XPATH, '//input[@value="post"]')
    MENU_CITY_SEARCH = (By.XPATH, '//span[@aria-labelledby="select2-js-data-example-ajax-container"]')
    FIELD_CITY_SEARCH = (By.XPATH, '//input[@class="select2-search__field"]')
    SELECT_RESULT_SEARCH = (By.XPATH, '//ul[@class="select2-results__options"]')
    FIELD_PLACEHOLDER_SEARCH = (By.XPATH, '//span[@class="select2-selection__placeholder"]')
    SELECT_PLACEHOLDER_SEARCH = (By.XPATH, '//li[@class="select2-results__option"][4]')
    SELECT_BTN_POSTPAID = (By.XPATH, '//input[@id="paymentmethod_1"]')
    BUTTON_PLACE_AN_ORDER = (By.XPATH, '//button[@data-complete="Оформити замовлення"]')

class SignupPageLocators:
    INPUT_NAME = (By.XPATH, '//input[@id="FirstName"]')
    INPUT_LASTNAME = (By.XPATH, '//input[@id="LastName"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="Email"]')
    INPUT_PHONE = (By.XPATH, '//input[@id="Phone"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="Password"]')
    INPUT_CONFIRM_PASSWORD = (By.XPATH, '//input[@id="ConfirmPassword"]')
    BUTTON_SIGNUP = (By.XPATH, '//button[@id="register-button"]')
    H2_SIGNUP = (By.XPATH, '//div[@class="page-title"]')
    ALERT_SUCCESS = (By.XPATH, '//div[text() = "Реєстрація завершена"]')

class LoginPageLocators:
    BUTTON_NEW_CLIENT = (By.XPATH, '//strong[text()="Новий клієнт"]')
    H1_LOGIN = (By.XPATH, '//div[@class="page-title"]')
    INPUT_EMAIL = (By.XPATH, '//input[@class="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@class="password"]')
    CHECKBOX_REMEMBERME = (By.XPATH, '//input[@type="checkbox"]')
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, '//a[@href="/ua/passwordrecovery"]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Увійти"]')
    BUTTON_WITHOUT_REGISTRATION = (By.XPATH, '//button[text()="Оформити замовлення без реєстрації"]')





#   pytest -s -v -m "main_page" --browser_mode="gui" --browser_name="firefox"
#               -m "signup_login_logout"   -m "order_page"
