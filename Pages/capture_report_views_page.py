import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class CaptureReportViewsPage:

    CAPTURE_VIEW_BUTTON = (By.ID, "capture-btn")
    SAVED_VIEWS_BUTTON = (By.ID, "display-btn")

    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay

    def _search_current_context(self, locator, depth=0):
        elements = self.driver.find_elements(*locator)

        if elements:
            return True

        if depth >= 3:
            return False

        frames = self.driver.find_elements(By.TAG_NAME, "iframe")

        for frame in frames:
            try:
                self.driver.switch_to.frame(frame)

                if self._search_current_context(locator, depth + 1):
                    return True

            except WebDriverException:
                pass

            finally:
                self.driver.switch_to.parent_frame()

        return False

    def _element_exists(self, locator):
        end_time = time.time() + self.delay

        while time.time() < end_time:
            self.driver.switch_to.default_content()

            if self._search_current_context(locator):
                self.driver.switch_to.default_content()
                return True

            time.sleep(0.5)

        self.driver.switch_to.default_content()
        return False

    def is_capture_view_present(self):
        return self._element_exists(self.CAPTURE_VIEW_BUTTON)

    def is_saved_views_present(self):
        return self._element_exists(self.SAVED_VIEWS_BUTTON)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title
