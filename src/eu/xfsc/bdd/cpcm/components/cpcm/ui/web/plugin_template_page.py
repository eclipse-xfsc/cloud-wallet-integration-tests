from playwright.sync_api import Page, expect
from .base_page import BasePage


class PluginTemplatePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.plugin_template_container = page.locator("//div[contains(@class,'d-flex')]")

    def plugin_template_container_present(self):
        expect(self.plugin_template_container).to_be_visible(timeout=5000)
