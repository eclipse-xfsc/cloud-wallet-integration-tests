from playwright.sync_api import Page, sync_playwright, expect
import asyncio

from .base_page import BasePage


class HistoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.history_table = page.locator("//div[contains(@class,'history')]")
        self.count = len(page.query_selector_all("table.undefined tbody tr"))
        self.amount = page.locator("//div[@class='d-flex justify-content-end']/span")

    def check_history_amount(self, history_length_random_number):
        print("history: ", history_length_random_number, "type: ", type(history_length_random_number))
        print("count: ", self.count, "type: ", type(self.count))
        assert self.count == history_length_random_number, "The counts do not match"

    def check_history_amount_0_empty(self):
        assert self.count == 0, "The counts do not match"

    def check_history_amount_max(self):
        amount = [int(s) for s in self.amount.text_content().split() if s.isdigit()]
        print(amount)

        assert amount[0] == amount[1], "The amount does not match"
        assert self.count == amount[0], "The counts do not match"

    def check_history_table(self):
        expect(self.history_table).to_be_visible(timeout=3000)
