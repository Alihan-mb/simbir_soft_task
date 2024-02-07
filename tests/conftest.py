import os
import time
from configurations.config import Test_Data
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

my_options = Options()
my_options.add_experimental_option("detach", True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = None
    option = None
    browser = request.config.getoption("browser")

    if browser == "chrome":
        option = ChromeOptions()
    elif browser == "firefox":
        option = FirefoxOptions()
    elif browser == "edge":
        option = EdgeOptions()
    else:
        print("Provide a valid browser name")

    driver = webdriver.Remote(
        command_executor="http://172.25.80.1:4444/wd/hub",
        options=option
    )
    request.cls.driver = driver
    driver.get(Test_Data.URL)
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            test_name = item.nodeid.split("::")[-1]
            file_name = time.strftime("{}_screen_%m_%d_%H-%M-%S_.png".format(test_name))
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    screenshot_folder = "reports"
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    file_path = os.path.join(screenshot_folder, name)
    driver.get_screenshot_as_file(file_path)