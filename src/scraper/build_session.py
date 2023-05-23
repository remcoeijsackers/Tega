# stolen from https://gist.github.com/stevenctl/d34e0494843479b2a12b9e58cf8d645e
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

SELENIUM_SESSION_FILE = './selenium_session'
SELENIUM_PORT=9515

def build_driver():
    options = Options()
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

    driver = webdriver.Chrome(options=options, port=SELENIUM_PORT)

    session_file = open(SELENIUM_SESSION_FILE, 'w')
    session_file.writelines([
        driver.command_executor._url,
        "\n",
        driver.session_id,
        "\n",
    ])
    session_file.close()

    return driver

#driver = build_driver()
#driver.get("https://google.com/")

# write whatever automated thing you need to do
# if you plan to re-run be sure that the actions are idempotent