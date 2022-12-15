import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#crea classe per sessione
class JustEat:
    def __init__(self, address):

        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.address = address

    def Address(self):
        # pagina dove inserire dati
        self.browser.get("https://www.justeat.it/")
        time.sleep(5)

        #dobbiamo cercare come gestire i cookie se serve
        self.browser.delete_all_cookies()

        #inseririsce dati nel form
        self.browser.find_element_by_class_name("Form_c-search-input_3ySg3").send_keys(address)

        #clicca la submit, non funziona, sintassi giusta, forse sono i cookie
        self.browser.find_element_by_class_name("Form_c-search-btn_2cjDI").submit()

        time.sleep(2)

#l'address successivamente lo prenderemo in input dall'index.html (guarda main)
address = "Via Andrea Angiulli, 47, 70126, Bari"

#queste linee di codice saranno nel main, ora sono qua per prova
# nel main importeremo le funzioni di scraper.py
mang = JustEat(address)
mang.Address()