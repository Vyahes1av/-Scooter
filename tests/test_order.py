import time
import allure
from pages.order_page import OrderPage
from conftest import driver
from data import Desing, Urls

class TestOrder:

    @allure.description("Проверка заполнения формы заказа")
    def test_order(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.order_page)
        order_page.set_name_input(Desing.Name)
        order_page.set_surname_input(Desing.Surname)
        order_page.set_address_input(Desing.Address)
        order_page.set_metro()
        order_page.set_number_input(Desing.Number)
        order_page.click_next_button()
        time.sleep(3)
        order_page.set_data()
        order_page.set_time()
        order_page.set_collor()
        order_page.set_comment(Desing.Comment)
        order_page.click_order_button()
        time.sleep(3)
        order_page.click_yes_button()

        assert order_page.order_pass()
