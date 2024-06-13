from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utils.json_helper import JsonHelper


class WebDriverFactory:
    @staticmethod
    def get_webdriver():
        browser_settings = JsonHelper().read_json('Configs/browser_settings.json')
        browser_name = browser_settings['browser']
        
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            for option in browser_settings['options']:
                options.add_argument(option)
            driver = webdriver.Chrome(options=options)

        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            for option in browser_settings['options']:
                options.add_argument(option)
            driver = webdriver.Firefox(options=options)
        
        driver.get(browser_settings['URL'])
        return driver
