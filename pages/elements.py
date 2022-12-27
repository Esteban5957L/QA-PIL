from pydoc import cli
from selenium.webdriver.common.by import By
class Page_element():
    def __init__(self, driver):
        self.driver = driver
        self.titleHome = "Thonet & Vander® :: Tecnología Alemana"
        self.home = (By.XPATH, '/html/body/header[1]/div[2]/div/div[1]/div')
        self.bookshelf = (By.XPATH, '//*[@id="contenido"]/div[1]/div[1]/ul/li[2]/a')

        self.support_list = (By.XPATH, '//*[@id="root"]/section/aside/div/ul/li[2]/span')
        self.support_list_click = (By.XPATH, '//*[@id="root"]/section/aside/div/ul/li[2]')
        self.support_request = (By.XPATH, '/html/body/div[1]/section/aside/div/ul/li[3]/span')
        self.first_element_list_click = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/table/tbody/tr[1]')
        self.todo1_inject = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]')
        self.add_files_toIject = (By.ID, 'file')
        self.next_button = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/button')
        self.inyecting_message = (By. XPATH, '/html/body/div[1]/section/section/main/div/div/h1')


    def complete_username(self,txt):
        return self.driver.find_element(*self.user_field).send_keys(txt)   

    def complete_password(self, txt):
        return self.driver.find_element(*self.pw_field).send_keys(txt)


    def login_button(self):
        return self.driver.find_element(*self.login_btn).click()

    def home_tooltip(self):
        return self.driver.find_element(*self.home).get_attribute('innerText')

    def bookshelf_tooltip(self):
        return self.driver.find_element(*self.bookshelf).get_attribute('href')

    def support_list_tooltip(self,todo = True):
        if todo:
            return self.driver.find_element(*self.support_list).get_attribute('innerText')
        return self.driver.find_element(*self.support_list_click).click()

    def support_request_tooltip(self):
        return self.driver.find_element(*self.support_request).get_attribute('innerText')

    def first_element_list(self):
        return self.driver.find_element(*self.first_element_list_click).click()

    def inject_click(self,todo):
        click = None
        if todo == 1:
            click = self.driver.find_element(*self.todo1_inject).click()
        return click

    def add_files(self, dir):
        return self.driver.find_element(*self.add_files_toIject).send_keys(dir)

    def nex_button_inject(self):
        return self.driver.find_element(*self.next_button).click()

    def inyection_in_progress(self):
        return self.driver.find_element(*self.inyecting_message).get_attribute('innerText')