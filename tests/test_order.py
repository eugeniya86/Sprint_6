import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage


@allure.feature("Флоу заказа самоката")
class TestOrderFlow:
    TEST_DATA = [
        (
            "верхняя кнопка",
            "Иван",
            "Петров",
            "ул. Ленина, 1",
            "Сокольники",
            "+79991112233",
            "01.01.2023",
            "сутки",
            "black",
            "Позвонить за час"
        )]
    TEST_DATA_2 = [
        (
            "нижняя кнопка",
            "Мария",
            "Сидорова",
            "пр. Мира, 10",
            "Черкизовская",
            "+79994445566",
            "10.01.2023",
            "двое суток",
            "grey",
            ""
        )
    ]

    @allure.title("Позитивный сценарий заказа - верхняя кнопка")
    @pytest.mark.parametrize(
        "entry_point,name,last_name,address,metro_station,phone,date,period,color,comment",
        TEST_DATA
    )
    def test_order_flow(
            self, driver, entry_point, name, last_name, address,
            metro_station, phone, date, period, color, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.accept_cookies()

        with allure.step(f"Нажать кнопку заказа ({entry_point})"):
            main_page.click_order_button_header()
        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(name, last_name, address, metro_station, phone)

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(date, period, color, comment)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить сообщение об успешном заказе"):
            assert "Заказ оформлен" in order_page.check_success_message()

        with allure.step("Проверить переход по логотипу Самоката"):
            main_page.click_scooter_logo()
            assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

        with allure.step("Проверить переход по логотипу Яндекса"):
            main_page.click_yandex_logo()
            assert "dzen.ru" in main_page.get_current_url()

    @allure.title("Позитивный сценарий заказа - нижняя кнопка")
    @pytest.mark.parametrize(
        "entry_point,name,last_name,address,metro_station,phone,date,period,color,comment",
        TEST_DATA_2
    )
    def test_order_flow_second(
            self, driver, entry_point, name, last_name, address,
            metro_station, phone, date, period, color, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.accept_cookies()

        with allure.step(f"Нажать кнопку заказа ({entry_point})"):
            main_page.click_order_button_footer()
        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(name, last_name, address, metro_station, phone)

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(date, period, color, comment)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить сообщение об успешном заказе"):
            assert "Заказ оформлен" in order_page.check_success_message()

        with allure.step("Проверить переход по логотипу Самоката"):
            main_page.click_scooter_logo()
            assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

        with allure.step("Проверить переход по логотипу Яндекса"):
            main_page.click_yandex_logo()
            assert "dzen.ru" in main_page.get_current_url()