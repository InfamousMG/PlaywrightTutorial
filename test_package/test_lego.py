import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.webqa.lego.com/pl-pl")
    page.locator("[data-test=\"age-gate-grown-up-cta\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"cookie-accept-all\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"header-account-cta\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"legoid-login-button\"]").click()
    time.sleep(5)
    page.get_by_placeholder("Nazwa użytkownika").click()
    time.sleep(5)
    page.get_by_placeholder("Nazwa użytkownika").fill("michal.gos@consultant.lego.com")
    time.sleep(5)
    page.get_by_placeholder("Nazwa użytkownika").press("Tab")
    time.sleep(5)
    page.get_by_placeholder("**********").fill("Legos54321!")
    time.sleep(5)
    page.get_by_test_id("loginBtn").click()
    time.sleep(5)
    expect(page.locator("[data-test=\"legoid-login-button\"]")).not_to_be_hidden()
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
