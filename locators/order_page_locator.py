
from selenium.webdriver.common.by import By

class OrderPageLocator:

    Head_order_page = (By.XPATH, "//div[1][text()='Для кого самокат']")
    Order_pass = (By.XPATH, "//div[text() ='Заказ оформлен']")
    Arenda_order = (By.XPATH, "//div[1][text()='Про аренду']")

    Button_next = (By.XPATH, "//button[text()= 'Далее']")
    Button_order = (By.XPATH, "//button[2][text()= 'Заказать']")
    Button_yes = (By.XPATH, "//button[2][text()= 'Да']")

#Страница 1
    Name_order = (By.XPATH, "//div[1]/input[@placeholder='* Имя']")
    Surname_order = (By.XPATH, "//div[2]/input[@placeholder='* Фамилия']")
    Address_order = (By.XPATH, "//div[3]/input[@placeholder='* Адрес: куда привезти заказ']")
    Metro_order = (By.XPATH, "//div[1]/input[@placeholder='* Станция метро']")
    Metro_click_stantion = (By.XPATH, "//li[7]/button[@value='7']")
    Iphone_order = (By.XPATH, "//div[5]/input[@placeholder='* Телефон: на него позвонит курьер']")



#Страница 2
    Data_order = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    Data_select = (By.XPATH, "//div[7][@aria-label='Choose воскресенье, 6-е октября 2024 г.']")
    Time_order = (By.CLASS_NAME, "Dropdown-control")
    Time_order_click = (By.XPATH, "//div[3][text()='трое суток']")
    Collor = (By.ID, "grey")
    Comments = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")


#/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[3]