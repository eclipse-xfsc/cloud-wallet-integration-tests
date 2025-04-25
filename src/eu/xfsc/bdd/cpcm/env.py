"""
Keep all OS env used.
"""
import os

from .defaults import PREFIX

# pylint: disable=line-too-long
WEB_UI_HOST = os.getenv(PREFIX + "_WEB_UI_HOST")
WEB_UI_ADMIN_USERNAME = os.getenv(PREFIX + "_WEB_UI_ADMIN_USERNAME")
WEB_UI_ADMIN_PWD = os.getenv(PREFIX + "_WEB_UI_ADMIN_PWD")
WEB_UI_TENANT_USERNAME = os.getenv(PREFIX + "_WEB_UI_TENANT_USERNAME")
WEB_UI_TENANT_PWD = os.getenv(PREFIX + "_WEB_UI_TENANT_PWD")


