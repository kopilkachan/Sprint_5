import pytest
from selenium import webdriver
import random 

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()

def random_mail():
    left_num = random.randint(0, 1000)
    right_num = random.randint(0, 1000)
    return f"random{left_num}@test{right_num}.com"