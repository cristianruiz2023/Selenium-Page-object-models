# generate by selenium ide

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPacientes():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_pacientes(self):
        driver.get("https://donboscolabs.com.ar")
        self.driver.set_window_size(1382,744)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "username").send_keys("mimail@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("laboratorio1")
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "loginButton").click()
        self.driver.find_element(By.LINK_TEXT, "Pacientes").click()
        self.driver.find_element(By.CSS_SELECTOR, ".table-primary:nth-child(1)>")
        self.driver.find_element(By.ID, "nombre").click()
        self.driver.find_element(By.ID, "nombre").send_keys("Pablo")
        self.driver.find_element(By.ID, "domicilio").click()
        self.driver.find_element(By.ID, "domicilio").send_keys("Santa fe 5050")
        self.driver.find_element(By.ID, "updateButton").click()
        assert driver.switch_to.alert.text == "Los datos se actualizaron correctamente"
        self.driver.find_element(By.LINK_TEXT, "volver").click()
        self.driver.find_element(By.LINK_TEXT, "volver").click()
        self.driver.find_element(By.LINK_TEXT, "inicio").click()
