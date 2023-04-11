import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.webqa.lego.com/pl-pl")
    page.locator("[data-test=\"age-gate-grown-up-cta\"]").click()
    page.locator("[data-test=\"cookie-accept-all\"]").click()
    page.locator("[data-test=\"header-account-cta\"]").click()
    page.locator("[data-test=\"legoid-login-button\"]").click()
    page.get_by_placeholder("Nazwa użytkownika").click()
    page.get_by_placeholder("Nazwa użytkownika").fill("michal.gos@consultant.lego.com")
    page.get_by_placeholder("Nazwa użytkownika").press("Tab")
    page.get_by_placeholder("**********").fill("Legos54321!")
    page.get_by_test_id("loginBtn").click()
    page.pause()
    expect(page.locator("[data-test=\"legoid-login-button\"]")).not_to_be_hidden()
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
