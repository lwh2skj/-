from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementNoLocatal:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_locator_error(self):
        '''
        ��λ����Ԫ��֤����λд����

        :return:
        '''
        self.driver.get("https://vip.ceshiren.com/")
        self.driver.find_element(By.ID,"xxx")