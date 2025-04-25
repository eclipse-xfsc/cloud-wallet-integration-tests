from behave import *
from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


@given("User is logged in")
def do_login_steps(context: TypedContex):
    context.ui.do_login_steps(context.page)


@step("User is on Settings screen")
def click_settings(context: TypedContex):
    context.ui.click_settings(context.page)


@given("language options is presented")
def lang_select_is_there(context: TypedContex):
    context.ui.settings_verify(context.page)


@when("the user changes language")
def change_lang(context: TypedContex):
    context.ui.change_lang(context.page)


@then("the cPCM is displayed in a different language")
def displayed_different_lang(context: TypedContex):
    context.ui.displayed_different_lang(context.page)


@given("history log option is presented")
def history_present(context: TypedContex):
    context.ui.history_present(context.page)


@when("the user selects a different length")
def input_different_length(context: TypedContex):
    context.ui.input_different_length(context.page)


@step("navigates to the event log")
def click_history(context: TypedContex):
    context.ui.click_history(context.page)


@then("the amount of events displayed matches the log length")
def check_amount(context: TypedContex):
    context.ui.check_history_amount(context.page)


@then("the amount of events displayed matches the log length for empty and zero")
def check_amount(context: TypedContex):
    context.ui.check_history_amount_0_empty(context.page)


@then("the amount of events displayed matches the log length for max")
def check_amount(context: TypedContex):
    context.ui.check_history_amount_max(context.page)


@when("the user selects an invalid value {value}")
def input_invalid_value(context: TypedContex, value):
    context.ui.input_different_length_invalid(context.page, value)


@when("the user selects an invalid alphabetical value {value}")
def input_invalid_value(context: TypedContex, value):
    context.ui.input_different_length_alphabetical(context.page, value)


@when("the user selects a different length of {length}")
def input_different_length(context: TypedContex, length: str):
    context.ui.input_different_length_invalid(context.page, str(length))


@then("error message is presented")
def step_impl(context: TypedContex):
    context.ui.toastify_error_present(context.page)
