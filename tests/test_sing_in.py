from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SING_IN, EMAIL, PASSWORD, AVATAR_USER, USER_NAME, LOGIN, LOG_OUT
from data import TestUser


class TestSingIn:
    def test_login_in_ex_acc_login(self, browser):
        browser.find_element(*SING_IN).click()  
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable(EMAIL))
        browser.find_element(*EMAIL).send_keys(TestUser.EMAIL)
        browser.find_element(*PASSWORD).send_keys(TestUser.PASSWORD)
        browser.find_element(*LOGIN).click()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable(AVATAR_USER))  
        assert browser.find_element(*AVATAR_USER).is_displayed() and browser.find_element(*USER_NAME).is_displayed()

    def test_logout_in_ex_acc_logout(self, browser):
        browser.find_element(*SING_IN).click()  
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable(EMAIL))
        browser.find_element(*EMAIL).send_keys(TestUser.EMAIL)
        browser.find_element(*PASSWORD).send_keys(TestUser.PASSWORD)
        browser.find_element(*LOGIN).click()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable(LOG_OUT))
        browser.find_element(*LOG_OUT).click()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable(SING_IN))
        assert len(browser.find_elements(*AVATAR_USER)) == 0
        assert len(browser.find_elements(*USER_NAME)) == 0
        assert browser.find_element(*SING_IN).is_displayed()

