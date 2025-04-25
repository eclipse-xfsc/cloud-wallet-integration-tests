from playwright.sync_api import Page, expect
from .base_page import BasePage



class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # top navbar
        self.verifyLoggedIn = page.locator("//nav[contains(@class,'WalletHeader_navbar')]")
        self.logoutIcon = page.locator("//div[contains(@class,'Header_account-icon')]")
        # sidebar
        self.sidebar = page.locator("//div[contains(@class,'WalletSideMenu_sidebar-wrapper')]")
        self.overview_btn = page.locator("//a[contains(@href,'credentials')]")
        self.issuance_btn = page.locator("//a[contains(@href,'issuance')]")
        self.presentation_selection_btn = page.locator("//a[contains(@href,'selection')]")
        self.presentations_btn = page.locator("//a[contains(@href,'presentations')]")
        self.offering_btn = page.locator("//a[contains(@href,'offering')]")
        self.settings_btn = page.locator("//a[contains(@href,'settings')]")
        self.plugin_overview_btn = page.locator("//a[contains(@href,'plugin-overview')]")
        self.pairing_management_btn = page.locator("//a[contains(@href,'pairing_management')]")
        self.identity_overview_btn = page.locator("//a[contains(@href,'did')]")
        self.backup_btn = page.locator("//a[contains(@href,'backup')]")
        self.plugin_template_btn = page.locator("//a[contains(@href,'Plugin-template')]")
        self.history_btn = page.locator("//a[contains(@href,'history')]")
        self.privacy_btn = page.locator("//a[contains(@href,'privacy')]")
        self.help_btn = page.locator("//a[contains(@href,'help')]")

    def check_if_logged_in(self):
        expect(self.verifyLoggedIn).to_have_count(1)

    def check_if_logout_visible(self):
        expect(self.logoutIcon).to_be_visible(timeout=5000)

    def check_sidebar_visible(self):
        expect(self.sidebar).to_be_visible()

    def click_overview(self):
        self.overview_btn.click()

    def click_issuance(self):
        self.issuance_btn.click()

    def click_presentation_selection(self):
        self.presentation_selection_btn.click()

    def click_presentations(self):
        self.presentations_btn.click()

    def click_offering(self):
        self.offering_btn.click()

    def click_settings(self):
        self.settings_btn.click()

    def click_plugin_overview(self):
        self.plugin_overview_btn.click()

    def click_pairing_management(self):
        self.pairing_management_btn.click()

    def click_identity_overview(self):
        self.identity_overview_btn.click()

    def click_backup(self):
        self.backup_btn.click()

    def click_plugin_template(self):
        self.plugin_template_btn.click()

    def click_history(self):
        self.history_btn.click()

    def click_privacy(self):
        self.privacy_btn.click()

    def click_help(self):
        self.help_btn.click()
