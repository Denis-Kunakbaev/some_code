from Utils.singleton_driver import BrowserSingleton
import pytest


@pytest.fixture(autouse=True, scope='function')
def browser():
    browser_instance = BrowserSingleton()
    yield browser_instance
    browser_instance.quit_driver()
    browser_instance = None