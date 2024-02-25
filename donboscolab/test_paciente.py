
#venv/mnt/42????/ext2/selenium/env_donbosco_pom
#test control de modificación de pacientes en DonBoscoLabs.com
#controla que la BD refleje los cambios realizados en el front-end

# imports.
import time
import json
from metodos import click_id, escribir_id,click_link,visitar_web,espera_implicita
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selectores import obtener_selector

driver = webdriver.Chrome()
#espera_implicita(driver,4)
espera_implicita(driver)
#espera implícita para todos los elementos

visitar_web("https://donboscolabs.com.ar")

driver.set_window_size(1382,744)

#importamos la función click_link de metodos.py
click_link(driver,"Login")


#se importa la función de métodos
escribir_id(driver,"username","mimail@gmail.com")
escribir_id(driver,"password","laboratorio1")

click_id(driver,"loginButton")


click_link(driver,"Pacientes")

driver.find_element(By.CSS_SELECTOR, ".table-primary:nth-child(1)> td:nth-child(4) img").click()

# funcion importada de metodos.py
escribir_id(driver,"nombre","maria")
# funcion importada de metodos.py
escribir_id(driver,"domicilio","calle cualquiera 5050")

driver.find_element(By.ID, "updateButton").click()

espera_explicita = WebDriverWait(driver,3)
#espera explicita de 3 seg a que aparezca la alerta
alerta = espera_explicita.until(EC.alert_is_present())#EC=espera explicita
alerta = driver.switch_to.alert #hace foco en la ventana del alerta

assert alerta.text == "Los datos se actualizaron correctamente"
# aserción del mensaje del alerta
alerta.accept()
time.sleep(2)

click_link(driver,"volver")
click_link(driver,"volver")
click_link(driver,"inicio")

driver.quit()
