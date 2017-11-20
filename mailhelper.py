from selenium.webdriver.common.keys import Keys


class MailHelper:

    def __init__(self, app):
        self.app = app

    def init_create_letter(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Написать письмо").click()

    def fill_receiver_address(self, address):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").click()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").clear()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").send_keys(address + ' ')

    def fill_letter_subject(self, subject):
        wd = self.app.wd
        element = wd.find_element_by_name("Subject")
        wd.execute_script("arguments[0].click();", element)  # из-за перекрытия элемента окошком с адресом
        wd.find_element_by_name("Subject").clear()
        wd.find_element_by_name("Subject").send_keys(subject)

    def fill_letter_text(self, text):
        wd = self.app.wd
        wd.switch_to.frame(wd.find_element_by_css_selector("td.mceIframeContainer>iframe"))
        wd.find_element_by_id("tinymce").click()
        wd.find_element_by_id("tinymce").clear()
        wd.find_element_by_id("tinymce").send_keys(text)
        wd.switch_to.default_content()

    def send_letter(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("body").send_keys(Keys.CONTROL + Keys.ENTER)

    def create_letter(self, letter):
        self.init_create_letter()
        self.fill_receiver_address(letter.address)
        self.fill_letter_subject(letter.subject)
        self.fill_letter_text(letter.text)
        self.send_letter()

    def get_assertion_text(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.message-sent__title").text