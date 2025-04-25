from behave import *
from playwright.sync_api import Page

from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


@given("sidebar is visible")
def check_sidebar_visible(context: TypedContex):
    context.ui.check_sidebar_visible(context.page)


@when("we have options selected randomly")
def random_selection(context):
    # this is just a placeholder to ensure the given-when-then structure
    # selecting random features happens in 'then' since it is easier
    pass


@then("the click selected options and check if loaded correctly")
def step_impl(context: TypedContex):
    context.ui.click_check_random_features(context.page)
