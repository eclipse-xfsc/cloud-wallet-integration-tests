from behave import *
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page


class TypedContex:
    ui: Ui
    page: Page


@when("we create an issuance with UUID and '{issuance_name}'")
def step_impl(context: TypedContex, issuance_name):
    context.ui.click_issuance(context.page)
    context.ui.issuance_verify(context.page)
    context.ui.click_select_schema(context.page)
    context.ui.fill_id(context.page)
    context.ui.fill_name(context.page, issuance_name)
    context.ui.click_submit_issuance(context.page)
    context.ui.save_issuance_link(context.page)
    context.ui.close_toastify(context.page)


@then("fill offering with link from issuance")
def step_impl(context: TypedContex):
    context.ui.click_offering(context.page)
    context.ui.offering_verify(context.page)
    context.ui.click_offering_add(context.page)
    context.ui.fill_offering_link_from_issuance(context.page)
    context.ui.click_offering_submit(context.page)
    context.ui.check_click_offering_accept(context.page)
    context.ui.select_did_option(context.page)
    context.ui.offering_accept_offering_accept(context.page)


@then("the credential added on overview with UUID")
def step_impl(context: TypedContex):
    context.ui.click_overview(context.page)
    context.ui.search_click_VC_from_issuance(context.page)
