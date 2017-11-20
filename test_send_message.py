# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def login(username, password):
    wd.find_element_by_id("mailbox:login").click()
    wd.find_element_by_id("mailbox:login").clear()
    wd.find_element_by_id("mailbox:login").send_keys(username)
    wd.find_element_by_id("mailbox:password").click()
    wd.find_element_by_id("mailbox:password").clear()
    wd.find_element_by_id("mailbox:password").send_keys(password)
    wd.find_element_by_css_selector("input.o-control").click()

def init_create_letter():
    wd.find_element_by_link_text("Написать письмо").click()

def fill_receiver_address(address):
    wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").click()
    wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").clear()
    wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").send_keys(address + ' ')

def fill_letter_subject(subject):
    element = wd.find_element_by_name("Subject")
    wd.execute_script("arguments[0].click();", element) #из-за перекрытия элемента окошком с адресом
    wd.find_element_by_name("Subject").clear()
    wd.find_element_by_name("Subject").send_keys(subject)

def fill_letter_text(text):
    wd.switch_to.frame(wd.find_element_by_css_selector("td.mceIframeContainer>iframe"))
    wd.find_element_by_id("tinymce").click()
    wd.find_element_by_id("tinymce").clear()
    wd.find_element_by_id("tinymce").send_keys(text)
    wd.find_element_by_id("tinymce").send_keys(Keys.CONTROL+Keys.ENTER)
    wd.switch_to.default_content()

def send_letter():
    #wd.find_element_by_css_selector("span.b-toolbar__btn__text").click()
    pass


def logout():
    wd.find_element_by_id("PH_logoutLink").click()


try:
    wd.get("https://mail.ru/")
    login(username="juk8738", password="U85HI7")
    init_create_letter()
    fill_receiver_address("virtus@quality-lab.ru")
    fill_letter_subject("Test letter")
    fill_letter_text("""Hello!
This is testing letter for checking e-mail sending via Python.
Best regards!""")
    send_letter()
    str = wd.find_element_by_css_selector("div.message-sent__title").text
    print(str)
    logout()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")


