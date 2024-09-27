
from selenium.webdriver.common.by import By

class MainPageLocator:


    Bottom_home_header = (By.XPATH, "//div[1][text()='Вопросы о важном']")

    Question_1 = (By.ID, 'accordion__heading-0')
    Question_2 = (By.ID, 'accordion__heading-1')
    Question_3 = (By.ID, 'accordion__heading-2')
    Question_4 = (By.ID, 'accordion__heading-3')
    Question_5 = (By.ID, 'accordion__heading-4')
    Question_6 = (By.ID, 'accordion__heading-5')
    Question_7 = (By.ID, 'accordion__heading-6')
    Question_8 = (By.ID, 'accordion__heading-7')

    Answer_1 = (By.ID, 'accordion__panel-0')
    Answer_2 = (By.ID, 'accordion__panel-1')
    Answer_3 = (By.ID, 'accordion__panel-2')
    Answer_4 = (By.ID, 'accordion__panel-3')
    Answer_5 = (By.ID, 'accordion__panel-4')
    Answer_6 = (By.ID, 'accordion__panel-5')
    Answer_7 = (By.ID, 'accordion__panel-6')
    Answer_8 = (By.ID, 'accordion__panel-7')


    button_form = (By.XPATH, "//div[5]/button[text()='Заказать']")




