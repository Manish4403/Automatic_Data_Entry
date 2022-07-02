import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Doc:
    def fill(self, price_list, link_list, address_list):
        driver_path = "/Users/manishsutradhar/Documents/chromedriver"
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        for i in range(len(price_list)):
            driver.get(
                "https://docs.google.com/forms/d/e/1FAIpQLSdanTu3kmh3jqEHeoMYEddNwblBfHmWtVVc2Vhh97INsOu8yQ/viewform?usp=sf_link")
            time.sleep(2)
            address = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(f"{address_list[i]}")

            price = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(f"{price_list[i]}")

            link = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(f"{link_list[i]}")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        driver.quit()
