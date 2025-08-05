# pages/base_page.py (дополненный)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)

    @allure.step("ждать элемент")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("проверить кликабельность")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}'")
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Проскроллить к элементу")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Проверить элемент")
    def is_element_displayed(self, locator, timeout=10):
        try:
            return self.wait_for_element(locator, timeout).is_displayed()
        except:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить количество открытых окон")
    def get_windows_count(self):
        return len(self.driver.window_handles)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, current_windows_count):
        self.wait.until(lambda d: len(d.window_handles) > current_windows_count)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание URL содержащего '{url_fragment}'")
    def wait_for_url_contains(self, url_fragment):
        self.wait.until(lambda d: url_fragment in d.current_url.lower())