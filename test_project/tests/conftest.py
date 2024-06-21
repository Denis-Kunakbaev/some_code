from utils.browser import Browser
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Название браузера (chrome, firefox)")

@pytest.fixture(autouse=True, scope='function')
def browser(request):
    browser_name = request.config.getoption("--browser")
    browser_instance = Browser(browser_name)
    yield browser_instance.get_driver()
    browser_instance.quit_driver()
