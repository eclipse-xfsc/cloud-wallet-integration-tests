from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, Browser, BrowserContext
from _datetime import datetime
from selenium import webdriver
import os


class TypedContext:
    page: Page
    browser: Browser
    selenium_driver: webdriver
    p: sync_playwright
    browser_type: str


def before_all(context: TypedContext):
    context.p = sync_playwright().start()


def before_scenario(context: TypedContext, scenario):
    # browser_type = context.config.userdata.get("browser", "chromium")
    context.browser_type = "chrome"

    if context.browser_type == "firefox":
        # firefox_executable_path = None

        # if os.name == 'nt':  # Windows
        #     firefox_executable_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        # elif os.name == 'posix':  # macOS and Linux
        #     if os.uname().sysname == 'Darwin':  # macOS
        #         firefox_executable_path = '/Applications/Firefox.app/Contents/MacOS/firefox'
        #     else:  # Linux
        #         firefox_executable_path = '/usr/bin/firefox'  # Adjust if needed

        # if not os.path.exists(firefox_executable_path):
        #     raise FileNotFoundError(f"Firefox executable not found at {firefox_executable_path}")

        # print(f"Launching Firefox from {firefox_executable_path}")  # Debugging info

        try:
            browser = context.p.firefox.launch(headless=False,
                                               #executable_path=firefox_executable_path,
                                               args=["--start-maximized"],
                                               slow_mo=1000)
            context.page = browser.new_page(no_viewport=True)
            context.browser = browser
            context.page.context.clear_cookies()
        except Exception as e:
            print(f"Failed to launch Firefox: {e}")
            raise e
    elif context.browser_type == "safari":
        print("Launching Safari")  # Debugging info

        try:
            context.selenium_driver = webdriver.Safari()
            context.selenium_driver.maximize_window()
            context.page = None
        except Exception as e:
            print(f"Failed to launch Safari: {e}")
            raise e
    elif context.browser_type == "webkit":
        browser = context.p.webkit.launch(headless=False,
                                          args=["--start-maximized"],
                                          slow_mo=1000)
        context.page = browser.new_page(no_viewport=True)
        context.browser = browser
        context.page.context.clear_cookies()
    else:
        browser = context.p.chromium.launch(headless=False,
                                            channel="chrome",
                                            args=["--start-maximized"],
                                            slow_mo=1000)
        context.page = browser.new_page(no_viewport=True)
        context.browser = browser
        context.page.context.clear_cookies()


def after_step(context, step):
    # timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # context.page.screenshot(path=f'screenshots/{step.name}_{timestamp}.png', full_page=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    if hasattr(context, 'selenium_driver') and context.selenium_driver:
        context.selenium_driver.save_screenshot(f'screenshots/{step.name}_{timestamp}.png')
    else:
        context.page.screenshot(path=f'screenshots/{step.name}_{timestamp}.png', full_page=True)


def after_scenario(context: TypedContext, scenario):
    # context.chrome.close()
    if hasattr(context, 'selenium_driver') and context.selenium_driver:
        context.selenium_driver.quit()
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()


def after_all(context: TypedContext):
    context.p.stop()
