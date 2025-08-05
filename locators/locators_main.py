from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH,
                           "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    questions_section = (By.CSS_SELECTOR, ".Home_FAQ__3uVm4")
