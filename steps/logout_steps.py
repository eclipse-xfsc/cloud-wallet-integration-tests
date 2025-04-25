from behave import *
#from behave.api.async_step import async_run_until_complete
from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui

use_step_matcher("re")


class TypedContex:
    ui: Ui
    page: Page


@given("the user successfully logged in to cPCM")
def do_login_steps(context: TypedContex):
    context.ui.do_login_steps(context.page)


@when("log out option is visible")
def check_logout_option(context: TypedContex):
    context.ui.check_logout_option(context.page)


@then('I logout')
def click_logout_button(context: TypedContex):
    context.ui.click_logout_button(context.page)


@then("I am logged out")
def verify_logged_out(context: TypedContex):
    context.ui.verify_logged_out(context.page)
