from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Search(unittest.TestCase):

    def setUp(self):
        self.drv=webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://www.google.com/ncr')

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        time.sleep(1)
        elm.send_keys(Keys.RETURN)
        time.sleep(2)
        assert 'selenide.org' in self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div').text
        self.drv.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[3]/a').click()
        time.sleep(2)
        assert 'selenide.org' in self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]').text
        self.drv.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
        time.sleep(1)
        assert 'selenide.org' in self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div').text

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()