
class BasePage():
    # конструктор класса - позволяет создать объект с обязательными полями
    # self - ссылка на сам, только что созданный, объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # неявное ожидание
        self.browser.implicitly_wait(timeout)

    # открыть страницу
    def open(self):
        self.browser.get(self.url)

    # сравнить текущий урл и ожидаемый
    def compare_urls(self, url):
        assert self.browser.current_url == url, "Текущий URL не совпал с ожидаемым"

