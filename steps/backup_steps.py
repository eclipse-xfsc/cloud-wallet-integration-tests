from behave import *

# from eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui
from playwright.sync_api import Page
from implementations.cpcm.src.eu.xfsc.bdd.cpcm.components.cpcm.ui import Ui


class TypedContex:
    ui: Ui
    page: Page


@step("User is on cPCM Wallet backup screen")
def step_impl(context: TypedContex):
    context.ui.click_backup(context.page)


@when("user create a backup in the UI with name '{backup_name}'")
def backup_create(context: TypedContex, backup_name):
    context.ui.click_add_backup(context.page)
    context.ui.fill_backup_name(context.page, backup_name)
    context.ui.click_submit_backup(context.page)


@then("scans the '{uploadORdownload}' link from screen")
def upload_QR_steps(context: TypedContex, uploadORdownload):
    context.ui.save_backup_QR(context.page, uploadORdownload)


@step("upload a file")
def step_impl(context: TypedContex):
    context.ui.QR_url_PUT(context.page)


@then("click the '{uploadORdownload}' with the matching name")
def step_impl(context: TypedContex, uploadORdownload):
    context.ui.reload_click_download(context.page)
    context.ui.save_backup_download_QR(context.page, uploadORdownload)


@step("download the file")
def step_impl(context: TypedContex):
    context.ui.QR_url_GET(context.page)


@then("compare files")
def step_impl(context):
    context.uploaded_content = context.ui.context.uploaded_content
    context.downloaded_content = context.ui.context.downloaded_content


@step("files are matching")
def step_impl(context):
    assert context.uploaded_content == context.downloaded_content, "The uploaded and downloaded files do not match."
