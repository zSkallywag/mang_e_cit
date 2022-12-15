import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class JustEat:
    def __init__(self, address):

        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.address = address

    def Address(self):
        # pagina dove inserire dati
        self.browser.get("https://www.justeat.it/")
        time.sleep(5)

        self.browser.delete_all_cookies()
        self.browser.find_element_by_class_name("Form_c-search-input_3ySg3").send_keys(address)
        self.browser.find_element_by_class_name("Form_c-search-btn_2cjDI").submit()

        time.sleep(2)

address = "Via Andrea Angiulli, 47, 70126, Bari"
mang = JustEat(address)
mang.Address()