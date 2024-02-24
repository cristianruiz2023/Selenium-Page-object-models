# procesamiento de multiples datos desde un archivo 
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#carga el driver del explorador
driver=webdriver.Chrome()
# maximiza la pantalla
driver.maximize_window()
#carga la url
driver.get("https://institutoweb.com.ar/test/login.html")

#leer acrivo con datos de login
with open('datos.json', 'r') as mis_datos:
    lector = json.load(mis_datos)
#se crea un bucle for para leer los renglones de datos   
    for renglon in lector:
        var_usuario = renglon['usuario']
        var_clave = renglon['clave']
        var_mail = renglon['mail']
        #print(f'usuario: {var_usuario} clave: {var_clave} mail: {var_mail}')
        #obtencion de los selectores
        txt_usuario = driver.find_element(By.ID,'tuusuario')
        txt_clave = driver.find_element(By.ID,'tuclave')
        txt_mail = driver.find_element(By.ID,'tumail')
        btn_ingresar = driver.find_element(By.CSS_SELECTOR,'body > form > button:nth-child(8)')
        ######### Acciones sobre los elementos ############
        txt_usuario.send_keys(var_usuario)
        txt_clave.send_keys(var_clave)
        txt_mail.send_keys(var_mail)
        btn_ingresar.click()
        ######## al acceso correcto volvemos a la pantalla login
        #obtencion de los selectores
        link_volver = driver.find_element(By.ID,'volver')
        title_ok = driver.find_element(By.CSS_SELECTOR,'body > h3')
        ####### asserciones
        text_asercion = f'usuario que fallo {renglon}'
        assert 'Acceso correcto!' == title_ok.text, text_asercion
        # el assert busca correcto en el h3 de body si lo encuentra no hace nada
        # si no lo encuenra lanza la asert error 'fallo el acceso
        ######## al acceso correcto volvemos a la pantalla login
        time.sleep(1)
        link_volver.click()
time.sleep(2)
driver.quit()   