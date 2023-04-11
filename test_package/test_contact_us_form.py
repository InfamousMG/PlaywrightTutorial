from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_page = ContactUsPage(page)
    contact_page.navigate()
    contact_page.submit_form("Michael", "123 Main Street")


# with sync_playwright() as playwright:
#     test_submit_form(playwright)
