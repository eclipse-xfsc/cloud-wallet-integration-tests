from playwright.sync_api import Page, expect
from qreader import QReader
import cv2
from datetime import datetime


class QRpage:
    def __init__(self, page: Page):
        self.page = page
        self.URLicon = page.locator("xpath=//div[@data-gtm-value='url']")
        self.URLinput = page.locator("xpath=//input[@formcontrolname='websiteUrl']")
        self.submitBtn = page.locator("xpath=//button[@data-js='generator-submit-btn']")
        self.URL = page.locator("xpath=//div[@class='ab-test-qrcode-wrapper']")
        self.cookies = page.locator("#onetrust-accept-btn-handler")
        self.telekom = page.locator("xpath=//a[@title='Telekom IT']")

    def nav_to_url_create(self):
        self.page.goto("https://hu.qr-code-generator.com/")

    def accept_cookies(self):
        self.cookies.click()

    def click_URL(self):
        self.URLicon.click()

    def enter_URL(self):
        self.URLinput.fill("https://www.telekom.com/")

    def click_submit(self):
        self.submitBtn.click()

    def save_scrnsht(self):
        self.page.locator("xpath=//div[@class='ab-test-qrcode-wrapper']").screenshot(path="invitation.png")
        self.page.screenshot(path="invitations/invitation.png")

    def read_from_QR(self):
        qreader = QReader()

        image = cv2.cvtColor(cv2.imread("invitations/invitation.png"), cv2.COLOR_BGR2RGB)

        # global destination
        destination = qreader.detect_and_decode(image=image)
        print(destination[0])
        return destination[0]

    def navigate_to_QR_url(self):
        destURL = self.read_from_QR()
        self.page.goto(destURL)

    def desired_page(self):
        expect(self.telekom).to_be_visible()
