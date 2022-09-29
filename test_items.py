from selenium.webdriver.common.by import By


def test_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = len(browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'))

    assert button > 0, "Not found button 'add-to-basket'"
