from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.env import WEB_UI_TENANT_PWD, WEB_UI_TENANT_USERNAME
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.usernameField = page.locator("#username")
        self.pwField = page.locator("#password")
        self.loginBtn = page.locator("#kc-login")

    def fill_username(self):
        self.usernameField.fill(WEB_UI_TENANT_USERNAME)

    def fill_password(self):
        self.pwField.fill(WEB_UI_TENANT_PWD)

    def fill_username_parallel(self, csv_username):
        self.usernameField.fill(csv_username)

    def fill_password_parallel(self, csv_password):
        self.pwField.fill(csv_password)

    def click_button(self):
        self.loginBtn.click()
