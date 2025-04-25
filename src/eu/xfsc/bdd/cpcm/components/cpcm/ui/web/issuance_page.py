from playwright.sync_api import Page, expect

from .base_page import BasePage


class IssuancePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.issuance_table = page.locator("//tr[@id='DeveloperCredential']")
        self.select_btn = page.locator("//td/button")
        self.unique_id_input = page.locator("//input[@id='root_given_name']")
        self.name_input = page.locator("//input[@id='root_family_name']")
        self.submit_btn = page.locator("//button[@type='submit']")
        self.copy_link_btn = page.locator("//div[@class='Toastify']//button[@class='btn btn-light']")
        self.issuance_link = page.locator("//div[@class='Toastify']//span")
        self.toastify_1 = page.locator("//div[@class='Toastify']//div[@id='1']//button[contains(@class,'Toastify__close-button')]")
        self.toastify_2 = page.locator("//div[@class='Toastify']//div[@id='2']//button[contains(@class,'Toastify__close-button')]")

    def issuance_table_present(self):
        expect(self.issuance_table).to_be_visible(timeout=5000)

    def click_select_schema(self):
        self.select_btn.click()

    def fill_id(self, issuance_id):
        expect(self.unique_id_input).to_be_visible(timeout=5000)
        self.unique_id_input.fill(issuance_id)

    def fill_name(self, issuance_name):
        expect(self.name_input).to_be_visible(timeout=5000)
        self.name_input.fill(issuance_name)

    def click_submit_issuance(self):
        self.submit_btn.click()

    def save_issuance_link(self) -> str:
        print(self.issuance_link.text_content())
        return self.issuance_link.text_content()

    def close_toastify(self):
        self.toastify_1.click()
        self.toastify_2.click()
