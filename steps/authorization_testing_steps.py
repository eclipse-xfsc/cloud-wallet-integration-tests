from behave import *

from playwright.sync_api import Page
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


@given("I am not logged in")
def step_impl(context: TypedContex):
    context.ui.open_url(context.page)


@when("User tries to access a restricted page")
def step_impl(context: TypedContex):
    context.ui.nav_to_credentials(context.page)


@then("User should be redirected to the login page")
def step_impl(context: TypedContex):
    current_url = context.ui.current_url(context.page)
    assert context.ui.login_base_url in current_url
