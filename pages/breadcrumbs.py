from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://magento.softwaretestingboard.com'
NAV_WOMEN = '//*[@id="ui-id-4"]'
NAV_TOPS = '//*[@id="ui-id-9"]'
NAV_JACKETS = '//*[@id="ui-id-11"]'
WOMEN_BREAD = '/html/body/div[2]/div[2]/ul/li[2]'
BREADCRUMBS = '/html/body/div[2]/div[2]/ul'

def open_page(driver):
    driver.get(URL)

def select_item(driver):
    actions = ActionChains(driver)
    women = driver.find_element(By.XPATH, NAV_WOMEN)
    tops = driver.find_element(By.XPATH, NAV_TOPS)
    jackets = driver.find_element(By.XPATH, NAV_JACKETS)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.move_to_element(jackets)
    actions.click(jackets)
    actions.perform()

def is_clickable(driver):
    driver.find_element(By.XPATH, WOMEN_BREAD).click()

def is_visible(driver):
    driver.find_element(By.XPATH, BREADCRUMBS).is_displayed()
    # driver.find_element(By.LINK_TEXT, "Women")
