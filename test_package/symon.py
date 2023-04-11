import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500) #slow-mo spowalnia działanie żeby było widać
    # co się dzieje, np. do debugowania
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000) # defaultowy timeout na wszystkie możliwe elementy oprócz asercji, bo tam
    # trzeba ustawiać osobno
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # expect(page.get_by_text("This site was designed")).to_be_visible() # asercja na napis na stronie
    # assert page.is_visible("text=This site was designed") # to ejst asercja pythonowa
    page.wait_for_load_state("networkidle") #to jak za szybko idzie test i się coś nie zdąży załadować na stronie
    # i czeka z resztą commandsów do wykonania, nie przechodzi dalej
    # # czekanie na selector
    page.get_by_role("button", name="Log In").click(timeout=2000)
    page.get_by_text("Log In").click()
    page.get_by_text("Shop Women", exact=True).click() # exact=True # to jak szukam elementu po tekście i chcę
    # żeby to był dokładnie taki tekst
    # time.sleep(5) # używanie tego nie jest dobrą praktyką
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click(timeout=50000)
    page.locator(":nth-match(input:below(:text('Email')), 1)").fill("abrakadabra", timeout=30000) # tutaj layoutowy
    # selector zmiksowany z nth match
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symonsterezhenko@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123", timeout=3000)
    # page.get_by_label("Password").press("Enter")
    page.pause() # pauzowanie w celu debugowania
    expect(page.get_by_role("button", name="Log In")).to_be_hidden() # to jest asercja playwrighta, assert to asercja
    # pythonowa
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
