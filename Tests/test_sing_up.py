from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SING_IN, NO_ACC, EMAIL, PASSWORD, REPEAT_PASSWORD, CREATE_ACC, AVATAR_USER, USER_NAME, ERROR_MESSAGE, ERROR_REPEAT_PASSWORD, ERROR_PASSWORD, ERROR_EMAIL
from conftest import random_mail

def test_sing_up_passed_login(browser):
    browser.find_element(*SING_IN).click() 
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(NO_ACC))  
    browser.find_element(*NO_ACC).click()
    browser.find_element(*EMAIL).send_keys(random_mail())
    browser.find_element(*PASSWORD).send_keys('parol')
    browser.find_element(*REPEAT_PASSWORD).send_keys('parol')
    browser.find_element(*CREATE_ACC).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(AVATAR_USER))  
    assert browser.find_element(*AVATAR_USER).is_displayed() and browser.find_element(*USER_NAME).is_displayed()

def test_sing_up_no_valid_mail_not_login(browser):
    browser.find_element(*SING_IN).click() 
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(NO_ACC))  
    browser.find_element(*NO_ACC).click()
    browser.find_element(*EMAIL).send_keys('nopomaske')
    browser.find_element(*PASSWORD).send_keys('parol')
    browser.find_element(*REPEAT_PASSWORD).send_keys('parol')
    browser.find_element(*CREATE_ACC).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(ERROR_MESSAGE))  
    assert browser.find_element(*ERROR_EMAIL).is_displayed() and browser.find_element(*ERROR_PASSWORD).is_displayed() and browser.find_element(*ERROR_REPEAT_PASSWORD) and browser.find_element(*ERROR_MESSAGE)

def test_sing_up_exist_user_not_valid(browser):
    browser.find_element(*SING_IN).click() 
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(NO_ACC))  
    browser.find_element(*NO_ACC).click()
    browser.find_element(*EMAIL).send_keys('1@1.com')
    browser.find_element(*PASSWORD).send_keys('parol')
    browser.find_element(*REPEAT_PASSWORD).send_keys('parol')
    browser.find_element(*CREATE_ACC).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(ERROR_MESSAGE))  
    assert browser.find_element(*ERROR_EMAIL).is_displayed() and browser.find_element(*ERROR_PASSWORD).is_displayed() and browser.find_element(*ERROR_REPEAT_PASSWORD) and browser.find_element(*ERROR_MESSAGE)
