from playwright.sync_api import Page, expect
from .base_page import BasePage


class PresentationSelectionPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.presentation_selection_table = page.locator("//table")
        self.select_presentation_btn = page.locator("//table//tr//button")
        self.credential_column = page.locator("//div[contains(@class,'CredentialColumn_presentation')]")
        self.presentation_selection_box = page.locator("//div[contains(@class,'PresentationSelection_selection-box')]")
        self.presentation_card = page.locator("//div[contains(@class,'CardDocument_card-document')]")
        self.presentation_card_family_name = page.locator("//div[@class='flex-nowrap row'][1]//strong")
        self.presentation_card_given_name = page.locator("//div[@class='flex-nowrap row'][2]//strong")
        self.DID_dropdown = page.locator("//select[@class='form-select']")
        self.presentation_selection_confirm_btn = page.locator("//button[contains(@class,'PresentationSelection')]")

    def presentation_selection_table_present(self):
        expect(self.presentation_selection_table).to_be_visible(timeout=5000)

    def click_select_presentation_button(self):
        self.select_presentation_btn.first.click()

    def credential_column_present(self):
        expect(self.credential_column).to_be_visible(timeout=5000)

    def presentation_selection_container_present(self):
        expect(self.presentation_selection_box).to_be_visible(timeout=5000)

    def drag_and_drop(self):
        self.presentation_card.first.drag_to(self.presentation_selection_box)

    def save_presentation_card_family_name(self) -> str:
        family_name = self.presentation_card_family_name.text_content()
        print(family_name)
        return family_name

    def save_presentation_card_given_name(self) -> str:
        given_name = self.presentation_card_given_name.text_content()
        print(given_name)
        return given_name

    def select_DID_dropdown(self):
        self.DID_dropdown.select_option(value='c0168bb0-29b7-48c7-9ad7-1d02958e727c')

    def click_presentation_selection_confirm(self):
        self.presentation_selection_confirm_btn.click()
