from behave import *

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page


class TypedContex:
    ui: Ui
    page: Page


@step("User is on Offering page")
def step_impl(context: TypedContex):
    context.ui.click_offering(context.page)
    context.ui.offering_verify(context.page)


@when("we click on Add button")
def step_impl(context: TypedContex):
    context.ui.click_offering_add(context.page)


@then("fill offering link with static url")
def step_impl(context: TypedContex):
    context.ui.fill_offering_link(context.page)


@then("fill offering link with invalid url")
def step_impl(context: TypedContex):
    context.ui.fill_offering_link_invalid(context.page)


@then("start listening for error on API lvl")
def step_impl(context: TypedContex):
    context.ui.verify_response(context.page)


@then("error message is presented on UI lvl")
def step_impl(context: TypedContex):
    context.ui.expected_error_present(context.page)


@when("click offering submit")
def step_impl(context: TypedContex):
    context.ui.click_offering_submit(context.page)


@then("an offering appears on screen and accept")
def step_impl(context: TypedContex):
    context.ui.check_click_offering_accept(context.page)


@then("clicked on accept and a DID selected")
def step_impl(context: TypedContex):
    context.ui.select_did_option(context.page)
    context.ui.offering_accept_offering_accept(context.page)
