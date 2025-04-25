from behave import *
from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


@step("User is on Presentation Selection page")
def step_impl(context: TypedContex):
    context.ui.click_presentation_selection(context.page)
    context.ui.presentation_selection_verify(context.page)


@when("user selects IDs for Presentation")
def step_impl(context: TypedContex):
    context.ui.select_id_for_presentation(context.page)


@step("selects the DID for Presentation")
def step_impl(context: TypedContex):
    context.ui.select_DID_dropdown_and_confirm(context.page)


@then("the presentation can be viewed by verifier")
def step_impl(context: TypedContex):
    context.ui.click_presentations(context.page)
    context.ui.check_add_from_presentation_selection_family_name(context.page)
    context.ui.check_add_from_presentation_selection_given_name(context.page)
