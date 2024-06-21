from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config_reader import ConfigReader


class WebDriverFactory:
    CHROME_NAME = 'chrome'
    FF_NAME = 'firefox'
    
    @staticmethod
    def get_options(browser_name):
        config = ConfigReader().get_config()
        
        if browser_name.lower() == WebDriverFactory.CHROME_NAME:
            options = ChromeOptions()
            for option in config['options']:
                options.add_argument(option)
            return options

        elif browser_name.lower() == WebDriverFactory.FF_NAME:
            options = FirefoxOptions()
            for option in config['options']:
                options.add_argument(option)
            return options
