from playwright.sync_api import Page, expect
from .base_page import BasePage


class PrivacyPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.privacy_table = page.locator("//table")

    def privacy_table_present(self):
        expect(self.privacy_table).to_be_visible(timeout=5000)
