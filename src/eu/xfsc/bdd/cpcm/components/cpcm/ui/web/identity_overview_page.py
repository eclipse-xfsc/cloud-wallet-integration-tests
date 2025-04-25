from playwright.sync_api import Page, expect
from .base_page import BasePage


class IdentityOverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.identity_overview_table = page.locator("//table")

    def identity_overview_table_present(self):
        expect(self.identity_overview_table).to_be_visible(timeout=5000)
