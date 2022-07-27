from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_card_button_exist(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    add_to_card_button = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    
    assert len(add_to_card_button) == 1, "\nКнопка добавления в корзину не отображается."
