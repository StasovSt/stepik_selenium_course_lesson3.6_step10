import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language:en/es/fr/ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart CHROME browser for test...")
        chromeOptions = ChromeOptions()
        chromeOptions.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chromeOptions)

    elif browser_name == "firefox":
        print("\nstart FIREFOX browser for test...")
        firefoxOptions = FirefoxOptions()
        firefoxOptions.set_preference("intl.accept_languages", user_language)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()
