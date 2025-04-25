from playwright.sync_api import Page, expect
from .base_page import BasePage


class PresentationsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.credential_column = page.locator("//div[contains(@class,'CredentialColumn')]")
        self.family_name_to_check = page.locator(f"//div[@class='flex-nowrap row'][1]//strong")
        self.given_name_to_check = page.locator(f"//div[@class='flex-nowrap row'][2]//strong")

    def presentation_selection_table_present(self):
        expect(self.credential_column).to_be_visible(timeout=5000)

    def check_add_from_presentation_selection_family_name(self, family_name):
        for element in self.family_name_to_check.element_handles():
            if element.inner_text() == family_name:
                return
        raise AssertionError(f"The following name not found: {family_name}")

    def check_add_from_presentation_selection_given_name(self, given_name):
        for element in self.given_name_to_check.element_handles():
            if element.inner_text() == given_name:
                return
        raise AssertionError(f"The following name not found: {given_name}")
