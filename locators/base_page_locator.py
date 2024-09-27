from selenium.webdriver.common.by import By

class BasePageLocator:

    Button_order = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    Button_form = (By.CSS_SELECTOR, ".Button_Button__ra12g Button_UltraBig__UU3Lp")
    Button_dzen = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    Button_scooter = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")


    Dzen = (By.XPATH, "//html[contains(@class, 'zen-page')]")