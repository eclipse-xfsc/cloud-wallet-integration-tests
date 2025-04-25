from playwright.sync_api import Page, expect
from .base_page import BasePage


class OfferingPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.offering_add_btn = page.locator("//button[@class='btn btn-primary']")
        self.static_url = "openid-credential-offer://?credential_offer=%7B%22credential_issuer%22%3A%22https%3A%2F%2Fcloud-wallet.xfsc.dev%22%2C%22credentials%22%3A%5B%22DeveloperCredential%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%22issuer_state%22%3A%22%22%7D%2C%22urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Apre-authorized_code%22%3A%7B%22pre-authorized_code%22%3A%22mJxZny5560Mltlkeu0GW%22%2C%22user_pin_required%22%3Afalse%7D%7D%7D"
        self.offering_input = page.locator("//input[@id='offeringLink']")
        self.offering_submit_btn = page.locator("//button[@type='submit']")
        self.offering_accept_btn = page.locator("//button[@data-type='accept']")
        self.offering_dropdown = page.locator("//select")
        self.accept_offering_did = page.locator("//button[@type='submit']")
        self.error_message = page.locator("//div[@class='modal-body']//p[contains(string(),'Error')]")

    def offering_add_btn_present(self):
        expect(self.offering_add_btn).to_be_visible(timeout=5000)

    def click_offering_add_btn(self):
        self.offering_add_btn.click()

    def fill_offering_link(self):
        self.offering_input.fill(self.static_url)

    def fill_offering_link_invalid(self):
        self.offering_input.fill("dog,cat,horse")

    def fill_offering_link_from_issuance(self, issuance_link):
        self.offering_input.fill(issuance_link)

    def click_offering_submit(self):
        self.offering_submit_btn.click()

    def verify_response(self):
        self.page.on("response", self._verify_response)

    def _verify_response(self, response):
        if "https://cloud-wallet.xfsc.dev/api/accounts/credentials/offers/create" in response.url:
            # print(response.url, response.status, response.text())
            try:
                if not response.status == 424:
                    # print(f"Raising exception because status is {response.status}")
                    raise Exception(f"Expected status 424 but got {response.status}")
            except Exception as e:
                print("Exception caught:", str(e))
                raise
            # response_text = response.text()
            # print("response_text: ", response_text)
            # assert "Failed Dependency" in response_text, f"Expected 'Failed Dependency' in response text but got {response_text}"

    def expected_error_present(self):
        expect(self.error_message).to_be_visible(timeout=5000)

    def check_click_offering_accept(self):
        expect(self.offering_accept_btn.first).to_be_visible(timeout=5000)
        self.offering_accept_btn.first.click()

    def select_did_option(self):
        self.offering_dropdown.select_option("c0168bb0-29b7-48c7-9ad7-1d02958e727c")

    def offering_accept_offering_accept(self):
        self.accept_offering_did.click()


