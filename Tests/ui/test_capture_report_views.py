import pytest


@pytest.mark.ui
def test_capture_view_button_is_present(capture_report_views_page):
    page = capture_report_views_page

    assert page.is_capture_view_present(), (
        f"Capture view button was not found. "
        f"URL: {page.get_current_url()}, "
        f"Title: {page.get_page_title()}"
    )


@pytest.mark.ui
def test_saved_views_button_is_present(capture_report_views_page):
    page = capture_report_views_page

    assert page.is_saved_views_present(), (
        f"Saved views button was not found. "
        f"URL: {page.get_current_url()}, "
        f"Title: {page.get_page_title()}"
    )
