from behave import *

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page


class TypedContex:
    ui: Ui
    page: Page


@given("credential cards are on screen")
def VC_cards_present(context: TypedContex):
    context.ui.overview_verify(context.page)


@when("the user clicks on a VC")
def click_VC(context: TypedContex):
    context.ui.click_VC(context.page)


@then("the selected VC details appear")
def check_VC_details(context: TypedContex):
    context.ui.check_VC_details(context.page)
