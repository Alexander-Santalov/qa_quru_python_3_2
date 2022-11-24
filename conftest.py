import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session')
def app():
    browser.open("https://google.com")
    browser.driver.maximize_window()
    yield browser
    browser.quit()
