import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#carga el driver del explorador
driver=webdriver.Chrome()
# maximiza la pantalla
driver.maximize_window()
#carga la url
driver.get("https://tienda.claro.com.ar")
txt_titulo = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')

assert 'Moto E13 64GB' == txt_titulo.text, 'el modelo no es el esperado'
print('Test exitoso')
driver.quit()