from playwright.sync_api import Page, sync_playwright, expect
from .base_page import BasePage


class SettingsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.lang_dropdown = page.locator("//select[@name='language']")
        self.html = page.locator("//html")
        self.save_changes_btn = page.locator("//button[@type='submit']")
        self.history_input = page.locator("//input[@name='historyLimit']")
        self.toastify_error = page.locator("//div[@role='alert']")

    def lang_select_is_there(self):
        expect(self.lang_dropdown).to_be_visible(timeout=5000)

    def change_lang(self):
        self.lang_dropdown.select_option("de")

    def click_save(self):
        self.save_changes_btn.click()

    def displayed_different_lang(self):
        currLang = self.html.get_attribute("lang")
        print(self.html.get_attribute("lang"))
        if currLang == "de":
            pass
        else:
            raise Exception("Selected and displayed language not matching")

    def history_present(self):
        expect(self.history_input).to_be_visible(timeout=5000)

    def input_different_length(self, history_length_random_number):
        self.history_input.fill(str(history_length_random_number))

    def input_invalid_value(self, history_length_invalid):
        self.history_input.fill(history_length_invalid)

    def input_invalid_alphabetical(self, page: Page, history_length_alphabetical):
        # page.evaluate(f'document.querySelector("{self.history_input}").value = "{history_length_alphabetical}";')
        # page.evaluate(f'document.querySelector("{self.history_input}").dispatchEvent(new Event("input"));')
        # is_valid = page.evaluate(f'document.querySelector("{self.history_input}").validity.valid')
        # return is_valid

        page.evaluate(f'''
            const inputElement = document.querySelector("input[name='historyLimit']");
            inputElement.value = "{history_length_alphabetical}";
            inputElement.dispatchEvent(new Event("input"));
        ''')

    def toastify_error_present(self):
        expect(self.toastify_error).to_be_visible(timeout=5000)

