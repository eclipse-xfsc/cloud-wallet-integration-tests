from playwright.sync_api import Page, expect

from .base_page import BasePage


class OverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.VC_cards = page.locator("//div[contains(@class, 'CardDocument')]")
        self.VC_card_present = page.wait_for_function("document.querySelectorAll('div[class*=\\'CardDocument\\']').length > 0")
        self.VC_modal = page.locator("//div[@class='modal-content']")
        self.json_data = page.locator("//code[@class='language-json']")

    def VC_cards_present(self):
        if self.VC_card_present:
            pass
        else:
            raise Exception("VC cards are not present")

    def click_VC(self):
        self.VC_cards.nth(0).click()

    def check_VC_details(self):
        expect(self.VC_modal).to_be_attached(timeout=5000)
        expect(self.json_data.nth(0)).to_be_visible(timeout=5000)
        expect(self.json_data.nth(1)).to_be_visible(timeout=5000)

    def search_click_VC_from_issuance(self, page: Page, issuance_id):
        VC_card_from_issuance = page.locator(f"//div[contains(@class,'CardDocument')]//strong[contains(text(),'{issuance_id}')]")
        expect(VC_card_from_issuance.first).to_be_visible(timeout=5000)
        VC_card_from_issuance.first.click()

