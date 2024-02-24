import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#carga el driver 
driver=webdriver.Chrome()
#carga la url
driver.get("https://institutoweb.com.ar/test/login.html")
#obtencion de los selectores
txt_usuario = driver.find_element(By.ID,'tuusuario')
txt_clave = driver.find_element(By.ID,'tuclave')
txt_mail = driver.find_element(By.ID,'tumail')

btn_ingresar = driver.find_element(By.CSS_SELECTOR,'body > form > button:nth-child(8)')

######### Acciones sobre los elementos ############



txt_usuario.send_keys('Mi_usuario'+ Keys.TAB)
txt_clave.send_keys('Mi_clave-123456')
txt_mail.send_keys('cris@cris.py')
time.sleep(2)
assert 'cris@cris.py' == txt_mail.get_attribute('value'), 'fallo el test'
time.sleep(2)

btn_ingresar.click()

time.sleep(2)
link_volver = driver.find_element(By.ID,'volver')
title_ok = driver.find_element(By.CSS_SELECTOR,'body > h3')
assert 'correcto' in title_ok.text, 'fallo el acceso se interrumpe el test'
# el assert busca correcto en el h3 de body si lo encuentra no hace nada
# si no lo encuenra lanza la asert error 'fallo el acceso
time.sleep(2)


print('test continua')# el print ocurrira si el test corre si tiene un fallo
#lanzara la assertionError "fallo el acceso"
link_volver.click()
driver.quit()