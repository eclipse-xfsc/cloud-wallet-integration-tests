import csv
import os
from playwright.sync_api import sync_playwright

CPCM_WEB_UI_ADMIN_USERNAME = os.environ.get("CPCM_WEB_UI_ADMIN_USERNAME")
CPCM_WEB_UI_ADMIN_PWD = os.environ.get("CPCM_WEB_UI_ADMIN_PWD")

def register_user(user_data, browser):

    context = browser.new_context()
    page = context.new_page()

    try:

        # Navigate to the registration page
        page.goto(f"https://{CPCM_WEB_UI_ADMIN_USERNAME}:{CPCM_WEB_UI_ADMIN_PWD}@cloud-wallet.xfsc.dev")
        page.locator("//div[contains(@class,'Footer_cookie-settings-container__ztPMW')]//button").click()
        page.locator("//div[@class='Header_account-icon-wrapper__hUxIt']").click()
        page.locator("//a[contains(@href,'registration')]").click()

        # Fill the registration form
        page.fill('input[name="firstName"]', user_data['firstname'])
        page.fill('input[name="lastName"]', user_data['lastname'])
        page.fill('input[name="email"]', user_data['email'])
        page.fill('input[name="username"]', user_data['username'])
        page.fill('input[name="password"]', user_data['password'])
        page.fill('input[name="password-confirm"]', user_data['confirm_password'])

        # Click the register button
        page.click("//input[@value='Register']")

        # Wait for navigation or response after registration
        page.wait_for_load_state("load")

        # Optional: check for success messages, redirections, etc.
        print(f"User: {user_data['username']} registered successfully.")

    except Exception as e:
        print(f"An error occurred while registering user {user_data['username']}: {str(e)}")

    finally:
        context.close()


def main():
    csv_file_path = 'users.csv'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome", args=["--start-maximized"])
        # page = browser.new_page(no_viewport=True)

        # Read user data from CSV file
        with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            headers = reader.fieldnames
            print("CSV Headers:", headers)  # Debug the headers
            first_row = next(reader, None)
            print("First row of data:", first_row)  # Debug the first row of data

            if not headers or not all(key in headers for key in ['firstname', 'lastname', 'email', 'username', 'password', 'confirm_password']):
                print("CSV file is missing some headers or has incorrect headers.")
            else:
                for user_data in reader:
                    register_user(user_data, browser)

        browser.close()


if __name__ == "__main__":
    main()
