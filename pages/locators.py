from selenium.webdriver.common.by import By


class BasePageLocators:
    PHONE = (By.XPATH, '//span[text()="+38 073 938 79 43"]')
    BUTTON_TELEGRAM = (By.XPATH, '//a[@class="social-logo telegram"]')
    ACCOUNT = (By.XPATH, '//div[@class="header-links-wrapper"]')
    MENU_REGISTRATION = (By.XPATH, '//a[@class="ico-register"]')
    MENU_LOGIN = (By.XPATH, '//a[@class="ico-login"]')
    MENU_WISHLIST = (By.XPATH, '//a[@class="ico-wishlist"]')

    LOGO_ = (By.XPATH, '//a[@class="logo"]')
    MAIN_MENU = (By.XPATH, '//a[text()="Головна"]')
    OPLATA_I_DOSTAVKA_MENU = (By.XPATH, '//ul[@class="top-menu"]//a[@href="/ua/oplata-i-dostavka"]')
    NEW_PRODUCTS_MENU = (By.XPATH, '//a[@href="/ua/newproducts"]')
    BESTCELLERY_MENU = (By.XPATH, '//ul[@class="top-menu"]//a[@href="/ua/newproducts"]')
    CONTACTS_MENU = (By.XPATH, '//a[@href="/ua/contactus"]')
    KOSHYK = (By.XPATH, '//a[@class="cart-trigger"]')
    INPUT_SEARCH = (By.XPATH, '//input[@id="small-searchterms"]')
    BUTTON_SEARCH = (By.XPATH, '//button[@type="submit"]')
    ####################################################################
    SUBSCRIBE = (By.XPATH, '//input[@placeholder="Введіть ваш email..."]')
    INPUT_SUBSCRIBE = (By.XPATH, '//button[@id="newsletter-subscribe-button"]')
    OPLATA_I_DOSTAVKA_FOOTER = (By.XPATH, '//div[@class="footer-block"]//a[text()="Оплата і доставка"]')
    AVTORY_FOOTER = (By.XPATH, '//a[text()="Автори"]')
    WAR_BOOK_FOOTER = (By.XPATH, '//div[@class="footer-block"]//a[text()="Військова книга"]')
    OSOBYSTYJ_KABINET_FOOTER = (By.XPATH, '//a[text()="Особистий кабінет"]')
    KOSHYK_FOOTER = (By.XPATH, '//a[text()="Кошик"]')


class MainPageLocators:
    BUTTON_HUDOJNJA_LITERATURA = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Художня література"]')
    BUTTON_WAR_BOOK = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Військова книга"]')
    BUTTON_KOMIKCY = (By.XPATH, '//div[@class="two-columns-area-left"]//a[text()="Комікси"]')
    SECTION_NEW_PRODUCTS = (By.XPATH, '//div[@class="page home-page"]/div/div[1]/div[@class="item-grid"]')
    NEW_BOOK_3 = (By.XPATH, '//div[@class="page home-page"]/div/div[1]/div[@class="item-grid"]/div[3]')
    BUTTON_POKAZAT_ESHCHO = (By.XPATH, '//a[text()="Показать еще"]')

    BUTTON_HITS_SEE_PREV = (By.XPATH, '//div[@id="jcarousel-3-488"]//button[@aria-label="Previous"]')
    BUTTON_HITS_SEE_NEXT = (By.XPATH, '//div[@id="jcarousel-3-488"]//button[@aria-label="Next"]')
    SECTION_HITS_PRODUCTS = (By.XPATH, '//div[@id="jcarousel-3-488"]')

    BUTTON_BESTSELLER_PREV = (By.XPATH, '//div[@id="jcarousel-4-302"]//button[@aria-label="Previous"]')
    BUTTON_BESTSELLER_NEXT = (By.XPATH, '//div[@id="jcarousel-4-302"]//button[@aria-label="Next"]')
    SECTION_BESTSELLER_PRODUCTS = (By.XPATH, '//div[@id="jcarousel-4-302"]')

    SECTION_POPULAR_AUTHORS = (By.XPATH, '//div[@class="product-grid"][2]')
    POPULAR_AUTHOR_1 = (By.XPATH, '//div[@class="product-grid"][2]//div[@class="item-box"][1]')
    BUTTON_ALL_AUTHORS = (By.XPATH, '//a[text()="Все авторы"]')

    SECTION_POPULAR_SERIES = (By.XPATH, '//div[@class="product-grid"][3]')
    POPULAR_SERIJA_3 = (By.XPATH, '//div[@class="product-grid"][3]//div[@class="item-box"][3]')
    BUTTON_ALL_SERIES = (By.XPATH, '//a[text()="Все серии"]')
    SECTION_ALL_SERIES = (By.XPATH, '//div[@class="category-grid home-page-category-grid"]')
    BUTTON_FICTION = (By.XPATH, '//a[text()=" Художня література "]')

    BUTTON_JOURNALS = (By.XPATH, '//a[text()="Все авторы"]')


