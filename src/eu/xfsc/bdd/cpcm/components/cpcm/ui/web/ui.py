from implementations.cpcm.src.eu.xfsc.bdd.cpcm.env import WEB_UI_ADMIN_PWD, WEB_UI_ADMIN_USERNAME
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.account_page import AccountPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.base_page import BasePage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.login_page import LoginPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.qr_page import QRpage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.settings_page import SettingsPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.history_page import HistoryPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.overview_page import OverviewPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.issuance_page import IssuancePage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.presentation_selection_page import PresentationSelectionPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.presentations_page import PresentationsPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.offering_page import OfferingPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.plugin_overview_page import PluginOverviewPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.pairing_management_page import PairingManagementPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.identity_overview_page import IdentityOverviewPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.backup_page import BackupPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.plugin_template_page import PluginTemplatePage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.privacy_page import PrivacyPage
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui.web.help_page import HelpPage
import requests
import random
import os
import uuid
from playwright.sync_api import Page

# variables to share across pages
history_length_random_number = random.randint(1, 10)
# history_length_invalid = 0
issuance_id = str(uuid.uuid4())


def random_feature_selection():
    features_list = ["click_overview", "click_issuance", "click_presentation_selection", "click_presentations", "click_offering", "click_settings", "click_plugin_overview", "click_pairing_management", "click_identity_overview", "click_backup", "click_plugin_template", "click_history", "click_privacy", "click_help"]
    features_num = random.randint(2, 5)

    selected_features = random.sample(features_list, features_num)
    print(selected_features)
    return selected_features


def split_at(what, char, num):
    words = what.split(char)
    return char.join(words[:num]), char.join(words[num:])


# def click_check_random_features():
#     # selected_features = self.random_feature_selection()
#     selected_features = ["click_settings, click_history"]
#
#     for feature in selected_features:
#         getattr(feature)()
#
#         # get the "feature's" name by splitting at first "_" and add "_verify" as next function to call
#         func_name = split_at(feature, "_", 1)[1]
#         verification_func = func_name + "_verify"
#         getattr(verification_func)


class Ui:
    def __init__(self, host: str, login_base_url: str, context) -> None:
        self.host = host
        self.login_base_url = login_base_url
        self.uname = WEB_UI_ADMIN_USERNAME
        self.pwd = WEB_UI_ADMIN_PWD
        self.variables = dict()
        self.context = context

    def is_up(self):
        response = requests.get(self.host, verify=False)  # + "/status")
        if not response.status_code == 200:
            if not response.status_code == 401:  # for FIREFOX
                raise AssertionError('is not up')

    def nav_to_credentials(self, page: Page):
        CPCM_WEB_UI_ADMIN_USERNAME = os.getenv("CPCM_WEB_UI_ADMIN_USERNAME")
        CPCM_WEB_UI_ADMIN_PWD = os.getenv("CPCM_WEB_UI_ADMIN_PWD")
        page.goto(f"https://{CPCM_WEB_UI_ADMIN_USERNAME}:{CPCM_WEB_UI_ADMIN_PWD}@cloud-wallet.xfsc.dev/en/wallet/credentials")

    def current_url(self, page: Page):
        return page.url

    # ----- HOME PAGE ----- #
    def open_url(self, page: Page):
        home_page = BasePage(page)
        home_page.navigate()
        home_page.accept_cookie()
        home_page.click_login()

    def click_logout_button(self, page: Page):
        home_page = BasePage(page)
        home_page.click_login()

    def verify_logged_out(self, page: Page):
        home_page = BasePage(page)
        home_page.check_if_logged_out()
    # ----- END:HOME PAGE ----- #

    # ----- LOGIN PAGE ----- #
    def fill_login(self, page: Page):
        login_page = LoginPage(page)
        login_page.fill_username()
        login_page.fill_password()

    def fill_login_parallel(self, page: Page, csv_username, csv_password):
        login_page = LoginPage(page)
        login_page.fill_username_parallel(csv_username)
        login_page.fill_password_parallel(csv_password)

    def do_login_step(self, page: Page):
        login_page = LoginPage(page)
        login_page.click_button()

    def check_if_logged_in(self, page: Page):
        account_page = AccountPage(page)
        account_page.check_if_logged_in()

    def do_login_steps(self, page: Page):
        login_page = LoginPage(page)
        home_page = BasePage(page)
        # page.context.clear_cookies()
        home_page.navigate()
        home_page.accept_cookie()
        home_page.click_login()
        login_page.fill_username()
        login_page.fill_password()
        login_page.click_button()
    # ----- END:LOGIN PAGE ----- #

    # ----- QR PAGE ----- #
    def nav_to_url_create(self, page: Page):
        qr_page = QRpage(page)
        qr_page.nav_to_url_create()
        qr_page.accept_cookies()

    def click_URL(self, page: Page):
        qr_page = QRpage(page)
        qr_page.click_URL()

    def enter_URL(self, page: Page):
        qr_page = QRpage(page)
        qr_page.enter_URL()

    def click_submit(self, page: Page):
        qr_page = QRpage(page)
        qr_page.click_submit()

    def save_scrnsht(self, page: Page):
        qr_page = QRpage(page)
        qr_page.save_scrnsht()

    def read_from_QR(self, page: Page):
        qr_page = QRpage(page)
        qr_page.read_from_QR()

    def navigate_to_QR_url(self, page: Page):
        qr_page = QRpage(page)
        qr_page.navigate_to_QR_url()

    def desired_page(self, page: Page):
        qr_page = QRpage(page)
        qr_page.desired_page()
    # ----- END:QR PAGE ----- #

    def click_check_random_features(self, page: Page):
        selected_features = random_feature_selection()
        # selected_features = ["click_settings", "click_history"]

        for feature in selected_features:
            getattr(self, feature)(page)

            # get the "feature's" name by splitting at first "_" and add "_verify" as next function to call
            func_name = split_at(feature, "_", 1)[1]
            verification_func = func_name + "_verify"
            getattr(self, verification_func)(page)

    # ----- ACCOUNT PAGE ----- #
        # ----- CLICK ON SIDE PANEL'S TABS ----- #
    def click_overview(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_overview()

    def click_issuance(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_issuance()

    def click_presentation_selection(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_presentation_selection()

    def click_presentations(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_presentations()

    def click_offering(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_offering()

    def click_settings(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_settings()

    def click_plugin_overview(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_plugin_overview()

    def click_pairing_management(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_pairing_management()

    def click_identity_overview(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_identity_overview()

    def click_backup(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_backup()

    def click_plugin_template(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_plugin_template()

    def click_history(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_history()

    def click_privacy(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_privacy()

    def click_help(self, page: Page):
        account_page = AccountPage(page)
        account_page.click_help()

        # ----- OTHER FUNCTIONS ON ACCOUNT PAGE ----- #
    def check_logout_option(self, page: Page):
        account_page = AccountPage(page)
        account_page.check_if_logged_in()
        account_page.check_if_logout_visible()

    def check_sidebar_visible(self, page: Page):
        account_page = AccountPage(page)
        account_page.check_sidebar_visible()
    # ----- END:ACCOUNT PAGE ----- #

    # ----- OVERVIEW PAGE ----- #
    def overview_verify(self, page: Page):
        overview_page = OverviewPage(page)
        overview_page.VC_cards_present()

    def click_VC(self, page: Page):
        overview_page = OverviewPage(page)
        overview_page.click_VC()

    def check_VC_details(self, page: Page):
        overview_page = OverviewPage(page)
        overview_page.check_VC_details()

    def search_click_VC_from_issuance(self, page: Page):
        overview_page = OverviewPage(page)
        overview_page.search_click_VC_from_issuance(page, issuance_id)
    # ----- END:OVERVIEW PAGE ----- #

    # ----- ISSUANCE PAGE ----- #
    def issuance_verify(self, page: Page):
        issuance_page = IssuancePage(page)
        issuance_page.issuance_table_present()

    def click_select_schema(self, page: Page):
        issuance_page = IssuancePage(page)
        issuance_page.click_select_schema()

    def fill_id(self, page: Page):
        issuance_page = IssuancePage(page)
        issuance_page.fill_id(issuance_id)

    def fill_name(self, page: Page, issuance_name):
        issuance_page = IssuancePage(page)
        issuance_page.fill_name(issuance_name)

    def click_submit_issuance(self, page: Page):
        issuance_page = IssuancePage(page)
        issuance_page.click_submit_issuance()

    def save_issuance_link(self, page: Page) -> str:
        issuance_page = IssuancePage(page)
        issuance_link_for_offer = issuance_page.save_issuance_link()
        self.variables.update({"issuance_link_for_offer": issuance_link_for_offer})
        return issuance_link_for_offer

    def close_toastify(self, page: Page):
        issuance_page = IssuancePage(page)
        issuance_page.close_toastify()

    # ----- END:ISSUANCE PAGE ----- #

    # ----- PRESENTATION SELECTION PAGE ----- #
    def presentation_selection_verify(self, page: Page):
        presentation_selection_page = PresentationSelectionPage(page)
        presentation_selection_page.presentation_selection_table_present()

    def select_id_for_presentation(self, page: Page):
        presentation_selection_page = PresentationSelectionPage(page)
        presentation_selection_page.click_select_presentation_button()

        # verify if both columns are present for drag and drop
        presentation_selection_page.credential_column_present()
        presentation_selection_page.presentation_selection_container_present()

        presentation_selection_page.drag_and_drop()

    def select_DID_dropdown_and_confirm(self, page: Page):
        presentation_selection_page = PresentationSelectionPage(page)

        family_name = presentation_selection_page.save_presentation_card_family_name()
        self.variables.update({"family_name": family_name})
        given_name = presentation_selection_page.save_presentation_card_given_name()
        self.variables.update({"given_name": given_name})

        presentation_selection_page.select_DID_dropdown()
        presentation_selection_page.click_presentation_selection_confirm()
    # ----- END:PRESENTATION SELECTION PAGE ----- #

    # ----- PRESENTATIONS PAGE ----- #
    def presentations_verify(self, page: Page):
        presentations_page = PresentationsPage(page)
        presentations_page.presentation_selection_table_present()

    def check_add_from_presentation_selection_family_name(self, page: Page):
        presentations_page = PresentationsPage(page)
        family_name = self.variables.get("family_name")
        print("given name from check : ", family_name)
        # family_name = "testName"
        presentations_page.check_add_from_presentation_selection_family_name(family_name)

    def check_add_from_presentation_selection_given_name(self, page: Page):
        presentations_page = PresentationsPage(page)
        given_name = self.variables.get("given_name")
        print("given name from check : ", given_name)
        # given_name = "MarkTest"
        presentations_page.check_add_from_presentation_selection_given_name(given_name)
    # ----- END:PRESENTATIONS PAGE ----- #

    # ----- OFFERING PAGE ----- #
    def offering_verify(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.offering_add_btn_present()

    def click_offering_add(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.click_offering_add_btn()

    def fill_offering_link(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.fill_offering_link()

    def fill_offering_link_invalid(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.fill_offering_link_invalid()

    def verify_response(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.verify_response()

    def expected_error_present(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.expected_error_present()

    def click_offering_submit(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.click_offering_submit()

    def fill_offering_link_from_issuance(self, page: Page):
        offering_page = OfferingPage(page)
        issuance_link = self.variables.get("issuance_link_for_offer")
        offering_page.fill_offering_link_from_issuance(issuance_link)

    def check_click_offering_accept(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.check_click_offering_accept()

    def select_did_option(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.select_did_option()

    def offering_accept_offering_accept(self, page: Page):
        offering_page = OfferingPage(page)
        offering_page.offering_accept_offering_accept()
    # ----- END:OFFERING PAGE  ----- #

    # ----- SETTINGS PAGE ----- #
    def settings_verify(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.lang_select_is_there()

    def change_lang(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.change_lang()
        settings_page.click_save()

    def displayed_different_lang(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.displayed_different_lang()

    def history_present(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.history_present()

    def input_different_length(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.input_different_length(history_length_random_number)
        settings_page.click_save()

    def input_different_length_invalid(self, page: Page, history_length_invalid):
        settings_page = SettingsPage(page)
        settings_page.input_invalid_value(history_length_invalid)
        settings_page.click_save()

    def input_different_length_alphabetical(self, page: Page, history_length_alphabetical):
        settings_page = SettingsPage(page)
        settings_page.input_invalid_alphabetical(page, history_length_alphabetical)
        # settings_page.click_save()

    def toastify_error_present(self, page: Page):
        settings_page = SettingsPage(page)
        settings_page.toastify_error_present()
    # ----- END:SETTINGS PAGE ----- #

    # ----- PLUGIN OVERVIEW PAGE ----- #
    def plugin_overview_verify(self, page: Page):
        plugin_overview_page = PluginOverviewPage(page)
        plugin_overview_page.plugin_overview_table_present()
    # ----- END:PLUGIN OVERVIEW PAGE ----- #

    # ----- PAIRING MANAGEMENT PAGE ----- #
    def pairing_management_verify(self, page: Page):
        pairing_management_page = PairingManagementPage(page)
        pairing_management_page.pairing_management_add_btn_present()
    # ----- END:PAIRING MANAGEMENT PAGE ----- #

    # ----- IDENTITY OVERVIEW PAGE ----- #
    def identity_overview_verify(self, page: Page):
        identity_overview_page = IdentityOverviewPage(page)
        identity_overview_page.identity_overview_table_present()
    # ----- END:IDENTITY OVERVIEW PAGE ----- #

    # ----- BACKUP PAGE ----- #
    def backup_verify(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.backup_table_present()

    def click_add_backup(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.click_add_backup()

    def fill_backup_name(self, page: Page, backup_name):
        backup_page = BackupPage(page, self.context)
        backup_page.fill_backup_name(backup_name)

    def click_submit_backup(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.click_backup_submit()

    def save_backup_QR(self, page: Page, createORdownload):
        backup_page = BackupPage(page, self.context)
        backup_page.save_backup_QR(createORdownload)

    def QR_url_PUT(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.QR_url_PUT()

    def reload_click_download(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.reload_click_download()

    def save_backup_download_QR(self, page: Page, uploadORdownload):
        backup_page = BackupPage(page, self.context)
        backup_page.save_backup_download_QR(uploadORdownload)

    def QR_url_GET(self, page: Page):
        backup_page = BackupPage(page, self.context)
        backup_page.QR_url_GET()


    # ----- END:BACKUP PAGE ----- #

    # ----- PLUGIN TEMPLATE PAGE ----- #
    def plugin_template_verify(self, page: Page):
        plugin_template_page = PluginTemplatePage(page)
        plugin_template_page.plugin_template_container_present()
    # ----- END:PLUGIN TEMPLATE PAGE ----- #

    # ----- HISTORY PAGE ----- #
    def check_history_amount(self, page: Page):
        history_page = HistoryPage(page)
        history_page.check_history_amount(history_length_random_number)

    def check_history_amount_0_empty(self, page: Page):
        history_page = HistoryPage(page)
        history_page.check_history_amount_0_empty()

    def check_history_amount_max(self, page: Page):
        history_page = HistoryPage(page)
        history_page.check_history_amount_max()

    def history_verify(self, page: Page):
        history_page = HistoryPage(page)
        history_page.check_history_table()
    # ----- END:HISTORY PAGE ----- #

    # ----- PRIVACY PAGE ----- #
    def privacy_verify(self, page: Page):
        privacy_page = PrivacyPage(page)
        privacy_page.privacy_table_present()
    # ----- END:PRIVACY PAGE ----- #

    # ----- HELP PAGE ----- #
    def help_verify(self, page: Page):
        help_page = HelpPage(page)
        help_page.help_table_present()
    # ----- END:HELP PAGE ----- #
