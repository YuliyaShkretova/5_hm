import allure
from allure_commons.types import Severity

from pages.registration import Registration
from data.user import user


def allure_decoration_steps(session):
    @allure.tag("Steps")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "YuliyaShkretova")
    @allure.feature("Checking form fill in")
    @allure.link("https://demoqa.com/automation-practice-form", name="HW_12")
    @allure.title("Тестирование заполнения анкеты и регистрации пользователя")
    def wrapper(*args, **kwargs):
        return session(*args, **kwargs)
    return wrapper


@allure.story('Регистрация по шагам')
@allure_decoration_steps
def test_form_fill_in():

    with allure.step('Open main page'):
        registration = Registration()
        registration.open()
    with allure.step('Fill in form'):
        registration.fill_in(user)
    with allure.step('Submit data'):
        registration.submit()
    with allure.step('Data checking'):
        registration.check(user)