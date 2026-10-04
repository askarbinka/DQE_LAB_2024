import os

import pytest
import yaml
from selenium import webdriver

from Pages.capture_report_views_page import CaptureReportViewsPage


def get_selenium_config():
    project_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    config_path = os.path.join(
        project_dir,
        "Configs",
        "config_selenium.yaml"
    )

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config["global"]


@pytest.fixture(scope="function")
def capture_report_views_page():
    config = get_selenium_config()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)

    driver.get(config["report_uri"])

    page = CaptureReportViewsPage(
        driver,
        int(config["delay"])
    )

    yield page

    driver.quit()