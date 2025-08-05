import allure

from .base_page import BasePage
from locators.locators_main import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть по кнопке 'Заказать'")
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликнуть по кнопке заказать, под самокатом")
    def click_order_button_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step("Кликнуть логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)
        self.wait.until(lambda d: d.current_url == "https://qa-scooter.praktikum-services.ru/")

    @allure.step("Кликнуть логотип Яндекса")
    def click_yandex_logo(self):
        current_windows = self.get_windows_count()  # Используем метод базового класса
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(current_windows)
        self.wait_for_url_contains("dzen.ru")

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Скролл до вопросов")
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.questions_section)
