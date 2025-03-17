from playwright.sync_api import Page, expect

def test_UIChecks(page:Page):
     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
     expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
     page.get_by_role("button", name="Hide").click()
     expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
     
     #alertboxes
     #lambda parameter:parameter.
     page.on("dialog", lambda dialog:dialog.accept())
     #page.get_by_role("alert", name="Confirm").click()
     page.get_by_role("button", name="Confirm").click()

     #hover
     page.locator("#mousehover").hover()
     page.get_by_role("link", name="Top").click()

     #Handling iFrame
     pageFrame = page.frame_locator("#courses-iframe")
     pageFrame.get_by_role("link", name="All Access Plan").click()
     expect(pageFrame.locator("body")).to_contain_text("Happy Subsciber")