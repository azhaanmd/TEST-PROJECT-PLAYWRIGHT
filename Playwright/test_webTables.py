from playwright.sync_api import Page, expect, Playwright
from time import sleep

def test_rice_price_from_table(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # This helped me to fix the HTTPS error of the URL
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceCol = index
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceCol)).to_have_text("37")