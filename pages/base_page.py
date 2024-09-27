from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Urls

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_text_and_find_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def wait_urls(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))



    def scroll_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def get_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

