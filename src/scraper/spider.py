from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logger = logging.getLogger(__name__)
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

        if wait:
            time.sleep(wait)

        if options:
            if "elemtype" in options:
                if options.get("elemtype") == "id":
                    try:
                        el = self.driver.find_element(By.ID, elem)
                    except:
                        logger.warning(f"could not find id {options.get('elemtype')}")
                if options.get("elemtype") == "class":
                    try:
                        el = self.driver.find_element(By.CLASS_NAME, elem)
                    except:
                        logger.warning(f"could not find class {options.get('elemtype')}")
        else:
            try:
                el = self.driver.find_element(By.ID, elem)
            except:
                logger.error(f"could not find id {options.get('elemtype')}")

        if wait:
            time.sleep(wait)

        el.click()
    
    def find_by_xpath(self):
        el = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input")
        x = el.get_property("value")
        return x


    def scrape_and_return(self, kwargs):
        """
        driver.get("https://temp-mail.org")
        """
        wait, value, elem, url, options = self.__fix_values(kwargs)

        if options and  "same_url" in options and not options.get("same_url"):
            self.driver.get(url)
        else:
            self.driver.get(url)
        
        time.sleep(10)

        try:
            el = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input")
            ret = el.get_property("value")
        except Exception as e:
            raise e("no element to click")
 
        if options and options.get("clean_up", None):
            self.driver.close()

        return ret
    

