# -*- coding: utf-8 -*-
import pytest
from letter import Letter
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_message(app):
    app.session.login(username="juk8738", password="U85HI7")
    app.mail.create_letter(Letter(address="virtus@quality-lab.ru", subject="Test letter", text="Hello!\nThis is testing "
    "letter for checking e-mail sending via Python.\nBest regards!"))
    assert app.mail.get_assertion_text() == "Ваше письмо отправлено. Перейти во Входящие"
    app.session.logout()



