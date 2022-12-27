import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pages.elements import *
import unittest


class Sprint3(unittest.TestCase):
    def setUp(self):
        s = Service('C:\dedge\msedgedriver.exe')
        self.driver = webdriver.Edge(service=s)

    
    def test_BluetoothSpeakers(self):
        self.driver.get('https://shop.thonet-vander.com/')
        self.driver.find_element(By.LINK_TEXT, "Bookshelf").click()
        title =  self.driver.title
        sleep(2)

        #verify bookshelf
        self.assertEqual("Bookshelf", title, '[ERROR] page Bookshelf')
        sleep(2)
        #assert "Bookshelfww" == title, "no es igual al titulo"

        self.driver.find_element(By.CSS_SELECTOR, ".logo:nth-child(1) img").click()
        sleep(2)

        title =  self.driver.title
        print(title)

        #verify homepage
        self.assertEqual("Thonet & Vander® :: Tecnología Alemana", title, '[ERROR] page homepage')
        sleep(2)
   
    def test_failGamers(self):
        self.driver.get('https://shop.thonet-vander.com/')
        self.driver.find_element(By.LINK_TEXT, "Home Theater").click()
        title =  self.driver.title
        sleep(2)
        print(title)

        #verify bookshelf
        self.assertNotEqual("Gamers", title, '[ERROR] page Bookshelf')
        sleep(2)
        #assert "Bookshelfww" == title, "no es igual al titulo"

        self.driver.find_element(By.CSS_SELECTOR, ".logo:nth-child(1) img").click()
        sleep(2)

        title =  self.driver.title
        print(title)

        #verify homepage
        self.assertEqual("Thonet & Vander® :: Tecnología Alemana", title, '[ERROR] page homepage')
        sleep(2)

    def test_Lanzamientos(self):
        self.driver.get('https://shop.thonet-vander.com/')
        self.driver.find_element(By.LINK_TEXT, "Lanzamientos").click()
        title =  self.driver.title
        sleep(2)

        #verify bookshelf
        self.assertEqual("Lanzamientos", title, '[ERROR] page Lanzamientos')
        sleep(2)
        #assert "Bookshelfww" == title, "no es igual al titulo"

        self.driver.find_element(By.CSS_SELECTOR, ".logo:nth-child(1) img").click()
        sleep(2)

        title =  self.driver.title
        print(title)

        #verify homepage
        self.assertEqual("Thonet & Vander® :: Tecnología Alemana", title, '[ERROR] page homepage')
        sleep(2)


    def tearDown(self):
        sleep(2)
        self.driver.quit()
        


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())