from playwright.sync_api import Page, expect
from time import sleep

#browers call API from UI -> API Provides Response (we can intercept here) > Browser uses the response  You have No Orders to show at this time.

dummy_no_order_payload = {"data":[],"message":"No Orders"}
dummy_test_order = {
    "data": [
        {
            "_id": "67db8ad9c019fb1ad62f5c5d",
            "orderById": "62742549e26b7e1a10e9fce0",
            "orderBy": "rahulshetty@gmail.com",
            "productOrderedId": "Thu Mar 20",
            "productName": "IPHONE 13 PRO",
            "country": "Bangladesh",
            "productDescription": "iphonenew",
            "productImage": "https://rahulshettyacademy.com/api/ecom/uploads/productImage_1650649561326.jpg",
            "orderDate": "null",
            "orderPrice": "231500",
            "__v": 0
        },
        {
            "_id": "67db8ad9c019fb1ad62f5c5a",
            "orderById": "62742549e26b7e1a10e9fce0",
            "orderBy": "rahulshetty@gmail.com",
            "productOrderedId": "Thu Mar 20",
            "productName": "ADIDAS ORIGINAL",
            "country": "Bangladesh",
            "productDescription": "Addias Originals",
            "productImage": "https://rahulshettyacademy.com/api/ecom/uploads/productImage_1650649488046.jpg",
            "orderDate": "null",
            "orderPrice": "31500",
            "__v": 0
        }
    ],
    "count": 2,
    "message": "Orders fetched for customer Successfully"
}
def intercept_response(route):
    route.fulfill(
        json = dummy_test_order
    )

def testNetwork_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response) #* is generic regex, whenever gets this url it triggers the event intercept_response
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    #sleep(60)
    # rows = page.locator("tr")
    # print("Row count:", rows.count())
    # for i in range(rows.count()):
    #     print(f"Row {i+1}: {rows.nth(i).text_content()}")

    # page.on("request", lambda request: print(f"Request: {request.url}"))
    # page.on("response", lambda response: print(f"Response: {response.url}"))
    expect(page.locator("tr")).to_have_count(3)
    # order_text = page.locator(".mt-4").text_content()
    # print(order_text)