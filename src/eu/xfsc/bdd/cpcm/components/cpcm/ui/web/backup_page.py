from playwright.sync_api import Page, expect
from .base_page import BasePage

from qreader import QReader
import cv2
import requests


def split_at(what, char, num):
    words = what.split(char)
    return char.join(words[:num]), char.join(words[num:])


def read_from_QR(uploadORdownload):
    qreader = QReader()

    image = cv2.cvtColor(cv2.imread(f"screenshots/backup/{uploadORdownload}.png"), cv2.COLOR_BGR2RGB)

    # global destination
    destination = qreader.detect_and_decode(image=image)
    print(destination[0])
    return destination[0]


def get_PUT_url():
    putURL = read_from_QR("upload")
    return putURL


def get_binding_id():
    # e.g. : ['http:', '', 'cloud-wallet.xfsc.dev', 'api', 'accounts', 'credentials', 'backup',
    # '4c216ab0-a91a-413f-8e97-a32eee7a4ef4', 'f3015a1a-049b-4a4e-b31e-9ce38e5326ca?']
    binding_id = get_PUT_url()
    binding_id = binding_id.split("/")
    # e.g. : 'f3015a1a-049b-4a4e-b31e-9ce38e5326ca?' --> 'f3015a1a-049b-4a4e-b31e-9ce38e5326ca'
    binding_id = binding_id[-1].rstrip("?")
    print(binding_id)
    return binding_id


def get_GET_url():
    getURL = read_from_QR("download")
    return getURL


class BackupPage(BasePage):

    def __init__(self, page: Page, context):
        super().__init__(page)
        self.backup_table = page.locator("//table")
        self.add_backup_btn = page.locator("//button[@class='btn btn-primary']")
        self.input_backup_name = page.locator("//input[@id='backupName']")
        self.backup_submit_btn = page.locator("//button[@type='submit']")
        self.current_id_download_btn = page.locator(f"//tr[@id='{get_binding_id()}']//button[@data-type='download']")
        self.context = context

    def backup_table_present(self):
        expect(self.backup_table).to_be_visible(timeout=5000)

    def click_add_backup(self):
        self.add_backup_btn.click()

    def fill_backup_name(self, backup_name):
        expect(self.input_backup_name).to_be_visible(timeout=5000)
        self.input_backup_name.fill(backup_name)

    def click_backup_submit(self):
        self.backup_submit_btn.click()

    def save_backup_QR(self, uploadORdownload):
        # self.page.locator("//div[@class='d-flex flex-column modal-body']").screenshot(path=f"{uploadORdownload}.png")
        self.page.screenshot(path=f"screenshots/backup/{uploadORdownload}.png")

    def QR_url_PUT(self):
        putURL = get_PUT_url()
        print("put url: ", putURL)
        string = 'MarkTestPayload some more string'
        payload = bytes(string, 'utf-8')
        print(payload)
        put_call = requests.put(putURL, data=payload, verify=False)
        self.context.uploaded_content = payload
        print("put text: ", put_call.text, " status code: ", put_call.status_code)

    def reload_click_download(self):
        self.page.reload()
        self.current_id_download_btn.click()

    def save_backup_download_QR(self, uploadORdownload):
        self.page.screenshot(path=f"screenshots/backup/{uploadORdownload}.png")

    def QR_url_GET(self):
        # getURL = get_GET_url()
        getURL = f"http://cloud-wallet.xfsc.dev/api/accounts/credentials/backup/link/download?bindingId={get_binding_id()}"
        get_call = requests.get(getURL, verify=False)
        print("get text: ", get_call.text)
        self.context.downloaded_content = get_call.content
