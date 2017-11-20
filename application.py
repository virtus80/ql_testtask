from selenium.webdriver.chrome.webdriver import WebDriver
from session import SessionHelper
from mailhelper import MailHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.mail = MailHelper(self)

    def destroy(self):
        self.wd.quit()

