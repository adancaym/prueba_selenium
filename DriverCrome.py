from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec


# Principio de una sola responsabilidad

# Principio de extención

# Principio de substitucion de liskov

class DriverCrome():
    def __init__(self, so='linux'):
        if so == 'linux':
            self.driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")
        if so == 'windows':
            self.driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver.exe")

    def get_elemento_by_css_esperar_a_presencia(self, css_selector):
        return WebDriverWait(self.driver, 2).until(Ec.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def get_elemento_by_css_esperar_a_que_sea_clickeable(self, css_selector):
        return WebDriverWait(self.driver, 2).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def get_elemento_by_css_esperar_a_que_sea_clickeable_and_send_keys(self, css_selector, keys):
        self.get_elemento_by_css_esperar_a_que_sea_clickeable(css_selector).send_keys(keys)

    def get_elemento_by_css_esperar_a_que_sea_clickeable_and_click(self, css_selector):
        self.get_elemento_by_css_esperar_a_que_sea_clickeable(css_selector).click()

    def get_elemento_by_css_and_send_keys(self, css_selector, keys):
        self.get_elemento_by_css_esperar_a_presencia(css_selector).send_keys(keys)

    def open_window_in_url(self, url):
        self.driver.get(url)

    def open_tab_and_switch(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_driver(self):
        self.driver.close()

    def find_element_by_link_text(self, text):
        return self.driver.find_element_by_link_text(text)

    def find_element_by_link_text_and_click(self, text):
        self.driver.find_element_by_link_text(text).click()

    def get_elemento_by_css_and_click(self, css_selector):
        self.get_elemento_by_css_esperar_a_presencia(css_selector).click()
