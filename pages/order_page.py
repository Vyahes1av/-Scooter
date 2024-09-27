import allure

from pages.base_page import BasePage
from locators.order_page_locator import OrderPageLocator
from locators.base_page_locator import BasePageLocator

class OrderPage(BasePage):


     @allure.step("Проверяем заголовок страницы после перехода по кнопке")
     def get_current_order_page(self, Head_page):
         curret_page = self.wait_text_and_find_element(OrderPageLocator.Head_order_page, Head_page)

         return curret_page.text

     @allure.step("Нажимаем кнопку Самокат")
     def click_element_scooter(self):
         element_button = self.wait_and_find_element(BasePageLocator.Button_scooter)
         element_button.click()



     @allure.step("Заполняем поле Имя")
     def set_name_input(self, name):
         name_input = self.wait_and_find_element(OrderPageLocator.Name_order)
         name_input.send_keys(name)

     @allure.step("Заполняем поле Фамилия")
     def set_surname_input(self, surname):
         surname_input = self.wait_and_find_element(OrderPageLocator.Surname_order)
         surname_input.send_keys(surname)

     @allure.step("Заполняем поле Адреса")
     def set_address_input(self, address):
         address_input = self.wait_and_find_element(OrderPageLocator.Address_order)
         address_input.send_keys(address)

     @allure.step("Выбираем станцию метро")
     def set_metro(self):
         metro_order = self.wait_and_find_element(OrderPageLocator.Metro_order)
         metro_order.click()


         metro_stantion = self.wait_and_find_element(OrderPageLocator.Metro_click_stantion)
         metro_stantion.click()

     @allure.step("Заполняем поле мобильного телефона")
     def set_number_input(self, number):
         number_input = self.wait_and_find_element(OrderPageLocator.Iphone_order)
         number_input.send_keys(number)

     @allure.step("Нажимаем кнопку далее")
     def click_next_button(self):
         button = self.wait_and_find_element(OrderPageLocator.Button_next)
         button.click()

     @allure.step("Выбираем дату")
     def set_data(self):
         data_1 = self.wait_and_find_element(OrderPageLocator.Data_order)
         data_1.click()

         data_2 = self.wait_and_find_element(OrderPageLocator.Data_select)
         data_2.click()

     @allure.step("Выбираем срок аренды")
     def set_time(self):
         time = self.wait_and_find_element(OrderPageLocator.Time_order)
         time.click()

         time_click = self.wait_and_find_element(OrderPageLocator.Time_order_click)
         time_click.click()

     @allure.step("Выбираем цвет")
     def set_collor(self):
         collor = self.wait_and_find_element(OrderPageLocator.Collor)
         collor.click()

     @allure.step("Оставляем комментарий к заказу")
     def set_comment(self, comment):
         comment_input = self.wait_and_find_element(OrderPageLocator.Comments)
         comment_input.send_keys(comment)

     @allure.step("Нажимаем кнопку Заказать")
     def click_order_button(self):
         button = self.wait_and_find_element(OrderPageLocator.Button_order)
         button.click()

     @allure.step("Нажимаем кнопку Да")
     def click_yes_button(self):
         button = self.wait_and_find_element(OrderPageLocator.Button_yes)
         button.click()

     @allure.step("Проверяем заголовок")
     def order_pass(self):
         element = self.wait_and_find_element(OrderPageLocator.Order_pass)
         return element.is_displayed()
