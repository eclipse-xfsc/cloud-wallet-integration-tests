from behave import *

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page


class TypedContex:
    ui: Ui
    page: Page


@given("navigate to QR generating page")
def nav_to_url_create(context: TypedContex):
    context.ui.nav_to_url_create(context.page)


@when("we created a QR code")
def step_impl(context: TypedContex):
    context.ui.click_URL(context.page)
    context.ui.enter_URL(context.page)
    context.ui.click_submit(context.page)


@step("saved it to our folder")
def step_impl(context: TypedContex):
    context.ui.save_scrnsht(context.page)


@then("we navigate to QR url")
def step_impl(context: TypedContex):
    context.ui.read_from_QR(context.page)
    context.ui.navigate_to_QR_url(context.page)


@step("we are at the desired page")
def step_impl(context: TypedContex):
    context.ui.desired_page(context.page)


@given("QR generating service working")
def step_impl(context):
    context.ui = Ui(
        host="https://hu.qr-code-generator.com/"
    )
    context.ui.is_up()
