import pytest
from selenium import webdriver
from data import TestUrl


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(TestUrl.HOME_URL)
    yield driver
    driver.quit()

