import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils import config

@pytest.mark.high
def test_dashboard_table_visible(browser):
    LoginPage(browser).open(config.BASE_URL)
    LoginPage(browser).login(username= config.USERNAME, password= config.PASSWORD)
    dashboard = DashboardPage(browser)
    assert dashboard.is_loaded()
