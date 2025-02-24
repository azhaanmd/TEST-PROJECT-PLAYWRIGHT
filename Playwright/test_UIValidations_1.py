from playwright.sync_api import Page, expect, Playwright
from time import sleep

def test_UIValidaitonsDynamicScripts(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-heading").filter(has_text="Nokia")).to_have_text("Nokia Edge")
    expect(page.locator(".media-heading").filter(has_text="iphone")).to_have_text("iphone X")
    sleep(3)


def test_childWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newpage_info:
        page.locator(".blinkingText").click()
        childPage = newpage_info.value
        text = childPage.locator(".red").text_content()
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
        print(text)