# from https://gist.github.com/stevenctl/d34e0494843479b2a12b9e58cf8d645e
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as firefox_options
import os

SELENIUM_SESSION_FILE = './selenium_session'
SELENIUM_PORT=9515

def build_driver(dtype=None):
    if dtype == "chrome":
        options = Options()
    else: 
        options = firefox_options()
    options.add_argument("--disable-infobars")
    options.add_argument("--enable-file-cookies")

    if os.path.isfile(SELENIUM_SESSION_FILE):
        session_file = open(SELENIUM_SESSION_FILE)
        session_info = session_file.readlines()
        session_file.close()

        executor_url = session_info[0].strip()
        session_id = session_info[1].strip()

        capabilities = options.to_capabilities()
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
        # prevent annoying empty chrome windows
        driver.close()
        driver.quit() 

        # attach to existing session
        driver.session_id = session_id
        return driver
    if dtype == "chrome":
        driver = webdriver.Chrome(options=options, port=SELENIUM_PORT)
    else:
        driver = webdriver.Firefox(options=options)

    session_file = open(SELENIUM_SESSION_FILE, 'w')
    session_file.writelines([
        driver.command_executor._url,
        "\n",
        driver.session_id,
        "\n",
    ])
    session_file.close()

    return driver
