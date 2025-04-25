from behave import *

from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


use_step_matcher("re")


@step("Open page and go login")
def step_impl(context: TypedContex):
    context.ui.open_url(context.page)


@when('I login with "(?P<csv_username>.+)" and "(?P<csv_password>.+)"')
def step_impl(context: TypedContex, csv_username, csv_password):
    context.ui.fill_login_parallel(context.page, csv_username, csv_password)
    context.ui.do_login_step(context.page)


@then("I should see the user dashboard")
def step_impl(context: TypedContex):
    context.ui.check_if_logged_in(context.page)
