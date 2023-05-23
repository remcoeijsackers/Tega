from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Jackson:
    def __init__(self, driver: webdriver.Firefox) -> None:
        self.driver = driver

    @staticmethod
    def __fix_values(values):
        wait, value, elem, url, options = None, None, None, None, None
        if "wait" in values:
            wait = values["wait"]
        if "elem" in values:
            elem = values["elem"]
        if "value" in values:
            value = values["value"]
        if "url" in values:
            url = values["url"]
        if "options" in values:
            options = values["options"]
        
        return wait, value, elem, url, options
    
    def click_and_return(self, kwargs):
        """
        """
        wait, value, elem, url, options = self.__fix_values(kwargs)

        self.driver.get(url)

        if options:
            if "elemtype" in options:
                if options.get("elemtype") == "id":
                    el = self.driver.find_element(By.ID, elem)
                if options.get("elemtype") == "class":
                    el = self.driver.find_element(By.CLASS_NAME, elem)
        else:
            el = self.driver.find_element(By.ID, elem)

        if wait:
            time.sleep(wait)

        el.click()

    def scrape_and_return(self, kwargs):
        """
        driver.get("https://temp-mail.org")

        time.sleep(10)
        elem = driver.find_element(By.ID, "mail")
        m = elem.get_attribute("value")
        print(m)
        """
        wait, value, elem, url, options = self.__fix_values(kwargs)

        if options:
            if "same_url" in options and not options.get("same_url"):
                self.driver.get(url)
        else:
            self.driver.get(url)

        if options:
            if "elemtype" in options:
                if options.get("elemtype") == "id":
                    el = self.driver.find_element(By.ID, elem)
                if options.get("elemtype") == "class":
                    el = self.driver.find_element(By.CLASS_NAME, elem)
        else:
            el = self.driver.find_element(By.ID, elem)

        if wait:
            time.sleep(wait)

        ret = el.get_attribute(value)
        print(ret)
        if options:
            if "clean_up" in options and options.get("clean_up"):
                self.driver.close()
        return ret
    

