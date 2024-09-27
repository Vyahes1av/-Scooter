import time

import allure
import pytest

from data import Urls, OrderData, MainData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver


class TestButten:


    @allure.description("Проверка перехода на страницу заказа по верхней кнопке 'Заказать'")
    def test_button_main_page_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page)
        main_page.click_element_order()

        order_page = OrderPage(driver)

        assert order_page.get_current_order_page(OrderData.Head_page) == OrderData.Head_page

    @allure.description("Проверка перехода на страницу заказа по нижней кнопке 'Заказать'")
    def test_button_main_page_form(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page)
        main_page.click_element_form()

        order_page = OrderPage(driver)

        assert order_page.get_current_order_page(OrderData.Head_page) == OrderData.Head_page

    @allure.description("Проверка перехода на основную страниу по кнопке 'Самокат'")
    def test_button_order_page_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.order_page)
        order_page.click_element_scooter()

        main_page = MainPage(driver)

        assert main_page.get_current_main_page(MainData.Head_page) == MainData.Head_page

    @allure.description("Проверка редиректа на страницу Дзена по кнопке 'Яндекс'")
    def test_button_main_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page)
        main_page.click_element_dzen()

        time.sleep(3)

        assert driver.current_url == Urls.redirected_page






