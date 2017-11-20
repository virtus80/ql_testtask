class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id("mailbox:login").click()
        wd.find_element_by_id("mailbox:login").clear()
        wd.find_element_by_id("mailbox:login").send_keys(username)
        wd.find_element_by_id("mailbox:password").click()
        wd.find_element_by_id("mailbox:password").clear()
        wd.find_element_by_id("mailbox:password").send_keys(password)
        wd.find_element_by_css_selector("input.o-control").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://mail.ru/")
