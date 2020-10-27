#!/usr/bin/python
# -*- coding: utf8 -*-
# author: David Martin

import os
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common import exceptions
import zipfile
import datetime
import shutil

# Modules
from config import config

# Proporciona tota la logica per treballar amb la Api de Selenium i realitzar
# operacions amb el navegador Chromedriver (obrir URL, descarregar arxius...)


class Browser:
    def __init__(self):
        self.browser = None
        self.base_path = config.base_path
        # Directori de descarrrega dels fitxers
        self.downpath = os.path.join(self.base_path, "downloads")
        self.display = Display(visible=0, size=(1280, 800))
        self.display.start()
        self.browser_init()

    def __del__(self):
        self.display.stop()

    def browser_init(self, downpath=None):
        if downpath is None:
            downpath = self.downpath

        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": downpath}
        chromeOptions.add_experimental_option("prefs", prefs)
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("--disable-dev-shm-usage")
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--ignore-certificate-errors")
        browser = webdriver.Chrome('chromedriver', chrome_options=chromeOptions)
        self.browser = browser


    def browser_check(self, downpath):
        if downpath is None:
            downpath = self.downpath
        else:
            self.downpath = downpath

        if downpath is not self.downpath and self.browser is not None:
            self.browser.close()

        if self.browser is None:
            self.browser_init(downpath)

    def browser_close(self):
        if self.browser is not None:
            self.browser.close()





