import os
import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    username = os.environ.get("username")
    password = os.environ.get("password")

    browser = p.chromium.launch(
        headless=False,
        channel="chrome",
        args=["--start-maximized"]
    )
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    #context.add_cookies([{'name': 'cookieSettings', 'value': 'true', 'path': '/', 'domain': '.xfsc.dev'}])
    page = context.new_page()

    page.goto(f"https://{username}:{password}@cloud-wallet.xfsc.dev/")

    acceptCookie = page.locator("xpath=//div[contains(@class,'Footer_cookie-settings-container__ztPMW')]//button")
    acceptCookie.click()

    loginBtn = page.locator("xpath=//div[@class='Header_account-icon-wrapper__hUxIt']")
    loginBtn.click()

    usernameField = page.locator("#username")
    pwField = page.locator("#password")

    usernameField.fill('test_user')
    pwField.fill('Qwerty123')

    inputBtn = page.locator("#kc-login")
    inputBtn.click()

    page.wait_for_load_state("domcontentloaded")
    verifyLoggedIn = page.locator("xpath=//nav[contains(@class,'WalletHeader_navbar')]")
    expect(verifyLoggedIn).to_have_count(1)
    time.sleep(3)

    loginBtn.click()

    expect(verifyLoggedIn).to_have_count(0)
    time.sleep(3)

    page.close()
    browser.close()
