import allure

from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator
from locators.base_page_locator import BasePageLocator
from data import Urls

class MainPage(BasePage):
    @allure.step("Скролим до 'Вопросы о важном' выбираем вопрос и нажимаем и проверяем текст")
    def set_scroll_and_click(self, question_locator, answer_locator):
        self.scroll_element(question_locator)
        self.click_element(question_locator)
        answer_element = self.wait_and_find_element(answer_locator)
        return answer_element.text
    @allure.step("Нажимаем верхнюю кнопку Заказать")
    def click_element_order(self):
        element_button = self.wait_and_find_element(BasePageLocator.Button_order)
        element_button.click()
    @allure.step("Нажимаем нижнюю кнопку Заказать")
    def click_element_form(self):
        self.scroll_element(MainPageLocator.button_form)
        self.click_element(MainPageLocator.button_form)
    @allure.step("Нажимаем кнопку Яндекс")
    def click_element_dzen(self):
        self.click_element(BasePageLocator.Button_dzen)
        self.wait_urls()
        self.get_window()
    @allure.step("Проверяем заголовок страницы после перехода")
    def get_current_main_page(self, Head_page):
        self.scroll_element(MainPageLocator.Bottom_home_header)
        curret_page = self.wait_text_and_find_element(MainPageLocator.Bottom_home_header, Head_page)

        return curret_page.text




