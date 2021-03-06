from selenium import webdriver
from base_element import BaseElement
from selenium.webdriver.common.by import By


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

