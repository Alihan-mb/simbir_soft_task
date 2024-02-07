import inspect
import logging
import os
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..'))  # Get absolute path of project directory

        log_file_path = os.path.join(project_dir, 'reports',
                                     'logfile.log')  # Construct path to log file relative to project directory

        fileHandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

