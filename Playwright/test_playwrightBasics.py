from playwright.sync_api import Page, expect, Playwright
from time import sleep
# def test_playwrightBasics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context() # This helped me to fix the HTTPS error of the URL
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")


# Page is a class fixture, from that we get page

#  Incorrect username/password.
# def test_playwrightPage(page:Page):
#     page.goto("http://www.rahulshettyacademy.com/") # chromium, 1 context, this is a shortcut, it runs in headless mode


def test_playwrightPage(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    sleep(5)


def test_checkWrongPass(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnin")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #sleep(5)



def test_fireforxBrowser(playwright: Playwright):
    fireforxBrowser = playwright.firefox
    browser = fireforxBrowser.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnin")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

