from behave import *

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page


class TypedContex:
    ui: Ui
    page: Page


@step("User is on Issuance page")
def be_on_issuance_page(context: TypedContex):
    context.ui.click_issuance(context.page)
    context.ui.issuance_verify(context.page)


@when("we click on select for a schema")
def click_select_schema(context: TypedContex):
    context.ui.click_select_schema(context.page)


@then("fill schema details with UUID and '{issuance_name}'")
def fill_schema_details(context: TypedContex, issuance_name):
    context.ui.fill_id(context.page)
    context.ui.fill_name(context.page, issuance_name)


@when("click submit")
def step_impl(context: TypedContex):
    context.ui.click_submit_issuance(context.page)


@then("we can copy a link to offer a credential")
def step_impl(context: TypedContex):
    context.ui.save_issuance_link(context.page)
