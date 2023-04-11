from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.get_by_role("button", name="Allow essential and optional cookies").click()
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("mmic.gss@gmail.com")
    page.get_by_test_id("royal_email").press("Tab")
    page.get_by_test_id("royal_pass").fill("damn")
    page.get_by_test_id("royal_login_button").click()
    expect(page.locator("id=login_link")).to_be_visible()
    print("Done")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)
