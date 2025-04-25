import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import jinja2

CPCM_WEB_UI_ADMIN_USERNAME = os.environ.get("CPCM_WEB_UI_ADMIN_USERNAME")
CPCM_WEB_UI_ADMIN_PWD = os.environ.get("CPCM_WEB_UI_ADMIN_PWD")


# Function to perform login
def login(username, password):


    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    result = {}

    try:
        # Open the site with embedded credentials
        driver.get(f"https://{CPCM_WEB_UI_ADMIN_USERNAME}:{CPCM_WEB_UI_ADMIN_PWD}@cloud-wallet.xfsc.dev")

        wait = WebDriverWait(driver, 10)  # Explicit wait up to 10 seconds

        # Wait for the cookies banner and accept cookies
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'Footer_cookie-settings-container__ztPMW')]//button")))
        accept_cookies_button.click()

        time.sleep(3)

        # Click on the login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Header_account-icon-wrapper__hUxIt']")))
        login_button.click()

        time.sleep(3)

        # Fill the username
        username_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username")))
        username_field.send_keys(username)

        time.sleep(3)

        # Fill the password
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys(password)

        time.sleep(3)

        # Click the login button
        login_submit_button = driver.find_element(By.CSS_SELECTOR, "#kc-login")
        login_submit_button.click()

        time.sleep(3)

        # Wait for the page to load and check if login was successful
        success_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//nav[contains(@class,'WalletHeader_navbar')]")))
        if success_element:
            print(f"Login successful for {username}")
            result['status'] = 'Success'
        else:
            print(f"Login failed for {username}")
            result['status'] = 'Failed'

    except Exception as e:
        print(f"Error logging in with {username}: {e}")
        result['status'] = 'Error'
        result['error'] = str(e)
    finally:
        driver.quit()
        result['username'] = username
        if 'error' not in result:
            result['error'] = ''  # Ensure error field exists
    return result


# Read users from CSV
def read_users_from_csv(file_path):
    df = pd.read_csv(file_path,delimiter=";")
    return df.to_dict('records')


# Main function to execute logins in parallel
def execute_parallel_logins(file_path, max_workers=5):
    users = read_users_from_csv(file_path)
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(login, user['username'], user['password']) for user in users]
        for future in futures:
            results.append(future.result())

    generate_html_report(results)


# Function to generate HTML report
def generate_html_report(results):
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 15px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Login Report</h2>
        <table>
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Status</th>
                    <th>Error</th>
                </tr>
            </thead>
            <tbody>
                {% for result in results %}
                <tr>
                    <td>{{ result.username }}</td>
                    <td>{{ result.status }}</td>
                    <td>{{ result.error }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """

    html_content = jinja2.Template(template).render(results=results)

    with open('login_report.html', 'w') as file:
        file.write(html_content)


if __name__ == "__main__":
    # max_workers define how many tests to run parallel (be gentle to your hardware)
    execute_parallel_logins('../users_selenium.csv', max_workers=5)
