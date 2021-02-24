from selenium.webdriver.common.by import By

class MainPageLocators():
    NAME = (By.CSS_SELECTOR, "input[name=name]")
    EMAIL = (By.CSS_SELECTOR, "input[name=email]")
    TEL = (By.CSS_SELECTOR, "input[name=phone]")
    MES = (By.CSS_SELECTOR, "textarea[name=message]")
    BUTTON = (By.CSS_SELECTOR, ".submit")
    ERR_MESSAGE = (By.CSS_SELECTOR, ".has-error")
    PASS_VALIDATION = (By.CSS_SELECTOR, ".feedback-page")
