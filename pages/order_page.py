import allure
from .base_page import BasePage
from locators.order_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу формы заказа")
    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.input_text(OrderPageLocators.METRO_STATION_INPUT, metro_station)
        self.click((OrderPageLocators.METRO_STATION_ITEM[0],
                    OrderPageLocators.METRO_STATION_ITEM[1].format(metro_station)))
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_second_page(self, date, period, color, comment):
        self.input_text(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN_ARROW)

        self.click((OrderPageLocators.RENTAL_PERIOD_OPTION[0],
                    OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period)))
        if color:
            self.click((OrderPageLocators.COLOR_CHECKBOX[0],
                        OrderPageLocators.COLOR_CHECKBOX[1].format(color)))
        if comment:
            self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_element(OrderPageLocators.CONFIRM_MODAL)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить успешное создание заказа")
    def check_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
