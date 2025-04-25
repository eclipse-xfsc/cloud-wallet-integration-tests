from playwright.sync_api import Page, expect
from .base_page import BasePage


class PluginOverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.plugin_overview_table = page.locator("//tr[@id='Plugin-template']")

    def plugin_overview_table_present(self):
        expect(self.plugin_overview_table).to_be_visible(timeout=5000)
