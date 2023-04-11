from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_elements import HomePage
import pytest

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # różne asercje
    home_page = HomePage(page)
    # expect(home_page.celebrate_header).to_be_visible()
    # expect(home_page.celebrate_body).to_be_visible()
    # assert page.is_visible("text=Celebrating Beauty and Style")
    # assert page.is_visible(home_page.celebrate_body) # nie działa, nie wiem dlaczego
    # assert page.locator(home_page.celebrate_body).is_visible() # nie działa, nie wiem dlaczego ale na pewno przez
    # element home_page.celebrate_body
    # assert page.locator("text=Celebrating Beauty and Style").is_hidden() # działa
    assert page.locator("text=Celebrating Beauty and Style").is_visible() # działa
    print("Done")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)

# zrobienie marka żeby skipować coś w teście
@pytest.mark.skip(reason="not ready")
def test_run_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # różne asercje
    home_page = HomePage(page)
    # expect(home_page.celebrate_header).to_be_visible()
    # expect(home_page.celebrate_body).to_be_visible()
    # assert page.is_visible("text=Celebrating Beauty and Style")
    # assert page.is_visible(home_page.celebrate_body) # nie działa, nie wiem dlaczego
    # assert page.locator(home_page.celebrate_body).is_visible() # nie działa, nie wiem dlaczego ale na pewno przez
    # element home_page.celebrate_body
    assert page.locator("text=Celebrating Beauty and Style").is_hidden() # działa
    # assert page.locator("text=Celebrating Beauty and Style").is_visible() # działa
    print("Done")

    # ---------------------
    context.close()
    browser.close()


# xfail oznacza że chcemy żeby test się wysypał i kiedy przechodzi normalnie to jest xfailed, a kiedy failuje to jest xpassed
@pytest.mark.xfail(reason="not ready")
def test_run_3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-13")
    page.set_default_timeout(3000)

    # różne asercje
    home_page = HomePage(page)
    # expect(home_page.celebrate_header).to_be_visible()
    # expect(home_page.celebrate_body).to_be_visible()
    # assert page.is_visible("text=Celebrating Beauty and Style")
    # assert page.is_visible(home_page.celebrate_body) # nie działa, nie wiem dlaczego
    # assert page.locator(home_page.celebrate_body).is_visible() # nie działa, nie wiem dlaczego ale na pewno przez
    # element home_page.celebrate_body
    assert page.locator("text=Celebrating Beauty and Style").is_hidden() # działa
    # assert page.locator("text=Celebrating Beauty and Style").is_visible() # działa
    print("Done")

    # ---------------------
    context.close()
    browser.close()