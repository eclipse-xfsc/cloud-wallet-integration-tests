from playwright.sync_api import Page, expect
from .base_page import BasePage


class PairingManagementPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.pairing_add_btn = page.locator("//button[contains(@class,'pairing-management')]")

    def pairing_management_add_btn_present(self):
        expect(self.pairing_add_btn).to_be_visible(timeout=5000)
