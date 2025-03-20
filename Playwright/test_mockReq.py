from playwright.sync_api import Page, expect, Playwright
from time import sleep
from utils.apiBase import APIUtils

#browers call API from UI (we can intercept here) -> API Provides Response  > Browser uses the response  You have No Orders to show at this time.
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67db8ad9c019fb1ad62f5c5z") #this orderid is from another account

def testmockReq(page:Page):
    page.on("request", lambda request:print(f'req: {request.url}'))
    page.on("response", lambda response:print(f'res {response.url}'))
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request) #* is generic regex, whenever gets this url it triggers the event intercept_response
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    
    sleep(5)
    nonAuthmessage = page.locator(".blink_me").text_content()
    print(nonAuthmessage)



def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()