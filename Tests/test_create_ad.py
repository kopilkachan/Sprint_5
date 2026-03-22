from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import SING_IN, EMAIL, PASSWORD, AVATAR_USER, LOGIN, PLACE_AN_AD, MODAL_WINDOW, PLACE_AN_AD, NAME_AD, DESCR, PRICE, DROPDOWN_BUTTON_CATEGORY, CATEGORY_SADOVOD, DROPDOWN_BUTTON_CITY , CITY_SPB, RADIO_BUTTON_BU, POST_AD, CARD_AD_PRICE, NEXT_BUTTON
import random 

def test_create_ad_not_login_window_login(browser):
    browser.find_element(*PLACE_AN_AD).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(EMAIL)) 
    assert browser.find_element(*MODAL_WINDOW).is_displayed()

def test_create_ad_ad_exist(browser):
    browser.find_element(*SING_IN).click()  
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(EMAIL))
    browser.find_element(*EMAIL).send_keys('poster@small.sw')
    browser.find_element(*PASSWORD).send_keys('aa')
    browser.find_element(*LOGIN).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(AVATAR_USER))  
    browser.find_element(*PLACE_AN_AD).click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(NAME_AD))
    browser.find_element(*NAME_AD).send_keys('Сущность Гномика')
    browser.find_element(*DROPDOWN_BUTTON_CATEGORY).click()
    browser.find_element(*CATEGORY_SADOVOD).click()
    browser.find_element(*RADIO_BUTTON_BU).click()
    browser.find_element(*DROPDOWN_BUTTON_CITY).click()
    browser.find_element(*CITY_SPB).click()
    browser.find_element(*DESCR).send_keys('Он не спит уже третьи сутки. Смотрит из угла. Забирайте сами, пока он не начал шевелиться. Сущность Гномика. Недорого')
    random_price = random.randint(0, 999)
    browser.find_element(*PRICE).send_keys(random_price)
    browser.find_element(*POST_AD).click()
    browser.get('https://qa-desk.stand.praktikum-services.ru/profile')
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(CARD_AD_PRICE))

    while True:
        try:
            next_button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(NEXT_BUTTON))
            if next_button.is_enabled():
                next_button.click()
            else: break
        except TimeoutException:
            break

    price_elements = browser.find_elements(*CARD_AD_PRICE)
    prices = [elem.text for elem in price_elements]
    assert f"{random_price} ₽" in prices
    