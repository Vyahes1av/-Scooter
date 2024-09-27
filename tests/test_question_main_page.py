import allure
import pytest

from data import Urls, TextQuestion
from pages.main_page import MainPage
from locators.main_page_locator import MainPageLocator
from conftest import driver

class TestQuestion:

    @allure.description('Проверка: Вопросы о важном')
    @pytest.mark.parametrize("question_locator, answer_locator, question_text", [
        (MainPageLocator.Question_1, MainPageLocator.Answer_1, TextQuestion.Text_1),
        (MainPageLocator.Question_2, MainPageLocator.Answer_2, TextQuestion.Text_2),
        (MainPageLocator.Question_3, MainPageLocator.Answer_3, TextQuestion.Text_3),
        (MainPageLocator.Question_4, MainPageLocator.Answer_4, TextQuestion.Text_4),
        (MainPageLocator.Question_5, MainPageLocator.Answer_5, TextQuestion.Text_5),
        (MainPageLocator.Question_6, MainPageLocator.Answer_6, TextQuestion.Text_6),
        (MainPageLocator.Question_7, MainPageLocator.Answer_7, TextQuestion.Text_7),
        (MainPageLocator.Question_8, MainPageLocator.Answer_8, TextQuestion.Text_8)
    ])
    def test_question_main_page(self, driver, question_locator, answer_locator, question_text):

        question_page = MainPage(driver)
        question_page.open_page(Urls.main_page)

        text_question = question_page.set_scroll_and_click(question_locator, answer_locator)
        assert text_question == question_text, f"Ответ на вопрос должен быть: {question_text}"

