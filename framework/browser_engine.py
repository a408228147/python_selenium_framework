import configparser
from selenium import  webdriver
import os.path
from framework.logger import Logger
import  time

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))#获取相对路径方法
    chrome_driver_path = dir +'/tools/chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver

      #read the browser type from config.ini file ,return the  driver
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s borwser." %browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is %s."% url)

        if browser =="Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser")
        elif browser =="Chrome":
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting chrome browser")
        elif browser =="IE":
            driver = webdriver.Chrome(self.ie_driver_path)
            logger.info("Starting ie browser")


        driver.get(url)
        logger.info("Open url:%s"%url)
        driver.maximize_window()
        logger.info("Maximize the current window")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self,driver):
        logger.info("Now Close and quit the borwser")
        driver.quit()

