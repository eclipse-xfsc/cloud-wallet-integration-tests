from behave import *
import os
#from behave.api.async_step import async_run_until_complete

from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page
    browser_type: str


@given("the user is on cPCM Login page")
def open_url(context: TypedContex):
    context.ui.open_url(context.page)


@given("input valid credentials provided")
def fill_login(context: TypedContex):
    context.ui.fill_login(context.page)


@when("login to cPCM")
def do_login_step(context: TypedContex):
    context.ui.do_login_step(context.page)


@then('the next page is Account page')
def is_next_page(context: TypedContex):
    context.ui.check_if_logged_in(context.page)


@given("Web UI cPCM is up")
def step_impl(context: TypedContex):

    CPCM_WEB_UI_ADMIN_USERNAME = os.environ.get("CPCM_WEB_UI_ADMIN_USERNAME")
    CPCM_WEB_UI_ADMIN_PWD = os.environ.get("CPCM_WEB_UI_ADMIN_PWD")

    if context.browser_type == "firefox":
        host = "https://cloud-wallet.xfsc.dev"
    else:
        host = f"https://{CPCM_WEB_UI_ADMIN_USERNAME}:{CPCM_WEB_UI_ADMIN_PWD}@cloud-wallet.xfsc.dev"

    print(host)

    context.ui = Ui(
        host=host,
        login_base_url="https://auth-cloud-wallet.xfsc.dev/realms/react-keycloak",
        context=context
    )
    context.ui.is_up()
