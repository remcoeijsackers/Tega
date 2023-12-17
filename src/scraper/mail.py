from .spider import Jackson
from selenium import webdriver
from .build_session import build_driver


def retrieve_disposable_mail(headless=True):
    options = webdriver.FirefoxOptions()
    options.headless = headless
    x = Jackson(webdriver.Firefox(options=options))

    return x.scrape_and_return(
        {
            "wait": 10,
            "value": "value",
            "elem": "mail",
            "url": "https://temp-mail.org",
            "options": {
                "clean_up": True 
            }
        }
    )


class MailMonitor():
    """
    If the selenium session is kept alive, the inbox is still viewable.
    """
    def __init__(self) -> None:
        self.jackson = Jackson(build_driver())
        self.__startup()

    def __startup(self):
        return self.jackson.scrape_and_return(
            {
                "wait": 10,
                "value": "value",
                "elem": "mail",
                "url": "https://temp-mail.org",
                "options": {
                    "clean_up": False,
                    "elemtype": "id"
                }
            }
        )

    def check_mail(self):
        self.jackson.click_and_return(
            {
                "wait": 10,
                "value": "value",
                "elem": "inboxSubject",
                "url": "https://temp-mail.org",
                "options": {
                    "clean_up": False,
                    "elemtype": "class"
                }
            }
        )
        return self.jackson.scrape_and_return(
            {
                "wait": 10,
                "value": "value",
                "elem": "user-data-subject",
                "url": "https://temp-mail.org",
                "options": {
                    "clean_up": False,
                    "elemtype": "class",
                    "same_url": True
                }
            }
        )
