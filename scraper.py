import time
from selenium import webdriver



class JustEat:
    def __init__(self, address):

        self.browser = webdriver.Chrome("/usr/bin/chromedriver")
        self.address = address

    def Address(self):
        # pagina dove inserire dati
        self.browser.get("https://www.justeat.com/")
        time.sleep(3)

        self.browser.find_element_by_class_name("Form_c-search-input_3ySg3").send_keys(address)

        time.sleep(2)

address = "Via Andrea Angiulli, 47, 70126, Bari"
mang = JustEat(address)
mang.Address()