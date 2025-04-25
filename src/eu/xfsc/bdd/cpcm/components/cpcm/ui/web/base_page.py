from playwright.sync_api import Page, expect
import os

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.env import WEB_UI_HOST, WEB_UI_ADMIN_PWD, WEB_UI_ADMIN_USERNAME


class BasePage:
    def __init__(self, page: Page):
        self.host = WEB_UI_HOST or "cloud-wallet.xfsc.dev"
        self.page = page
        self.uname = WEB_UI_ADMIN_USERNAME
        self.pwd = WEB_UI_ADMIN_PWD
        self.acceptCookie = page.locator("//div[contains(@class,'Footer_cookie-settings-container__ztPMW')]//button")
        self.accountBtn = page.locator("//div[@class='Header_account-icon-wrapper__hUxIt']")
        self.verifyLoggedOut = page.locator("//nav[contains(@class,'WalletHeader_navbar')]")

    def navigate(self):
        # self.page.goto("http://localhost:3000")
        self.page.goto(f"https://{self.uname}:{self.pwd}@cloud-wallet.xfsc.dev/")

    def accept_cookie(self):
        self.acceptCookie.click()

    def click_login(self):
        self.accountBtn.click()

    def check_if_logged_out(self):
        expect(self.verifyLoggedOut).to_have_count(0)

