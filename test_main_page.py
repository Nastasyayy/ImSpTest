from .pages.main_page import MainPage

def test_spacebar_input_in_fildes_besides_email(browser):
    link = "http://test-form.sibirix.ru/"
    page = MainPage(browser, link)
    page.open()
    page.spacebar_input()
