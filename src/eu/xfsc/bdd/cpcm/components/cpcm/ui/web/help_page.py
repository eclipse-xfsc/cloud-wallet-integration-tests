from playwright.sync_api import Page, expect
from .base_page import BasePage


class HelpPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.help_table = page.locator("//table")

    def help_table_present(self):
        expect(self.help_table).to_be_visible(timeout=5000)
