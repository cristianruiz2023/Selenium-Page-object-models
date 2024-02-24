#
# imports.
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selectores import obtener_selector
# le ponemos un alias EC porque es muy largo el nombre.

try:
    from selenium.webdriver.support import expected_conditions as EC
    # carga del driver browser
    driver = webdriver.Chrome()

    driver.implicitly_wait(4)#todas llevan 4 seg por convención.

    driver.maximize_window()
    driver.get('https://donboscolabs.com.ar')
    time.sleep(1)

    with open('datos.json', 'r') as mis_datos:
        lector = json.load(mis_datos)
# se crea un bucle for para leer los renglones de datos.   
        driver.find_element(By.LINK_TEXT,'Login').click()
        # variable que llama a la funcion que tiene como retorno los selectores
        login_screen = obtener_selector()

        for renglón in lector:
            var_usuario = renglón['usuario']
            var_clave = renglón['clave']
            # ventana de login de usuario.
            driver.find_element(By.ID,login_screen['input_usuario']).clear()
            # se agrega .clear()porque 'send_keys' concatena la escritura.
            driver.find_element(By.ID,login_screen['input_usuario']).send_keys(var_usuario)
            driver.find_element(By.ID,login_screen['input_password']).clear()
            driver.find_element(By.ID,login_screen['btn_ingresar']).click()
            driver.find_element(By.ID,login_screen['input_password']).send_keys(var_clave)

            # damos una espera implícita de manera global de 5 deg.
            # espera explicita solo para este elemento o proceso.
            espera_explicita = WebDriverWait(driver,2) # le decimos al driver que espera 2 seg
            alerta = espera_explicita.until(EC.alert_is_present())# EC= expected_condition
            # cambia el foco en el alerta.
            alerta = driver.switch_to.alert
            assert alerta.text == 'Usuario o Clave inválida'# aserción del texto del alert
            # click en aceptar de la ventana de alert.
            alerta.accept()
            time.sleep(1)
            # driver.find_element(By.LINK_TEXT,'Inicio').click().
            #para no recargar la web por cada iteración se pone .clear() en los campos.
# # excepción de assert.
# except AssertionError as ae:
#         print(f"Error de aserción: {str(ae)}")
#         driver.quit()
# #tiempo de espera.   
# #      
# except TimeoutException:
#     print("No se encontró el alerta dentro del tiempo especificado")
#     driver.quit()
# #excepción de elemento no encontrado.

# except NoSuchElementException as e:
#     print(f"Elemento no encontrado: {str(e)}")
#     driver.quit()
# # exception de file.

# except FileNotFoundError:
#     print("Archivo JSON no encontrado")
#     driver.quit()
# #excepción genérica cuando lo demás no corresponde.

# except Exception as e:
#     print(f"Ocurrió una excepción no manejada: {str(e)}")
#     driver.quit()

except AssertionError:
    print('existe un error de aserción')
except FileNotFoundError:
    print('no se encuentra el archivo de datos')
except Exception as mensaje:
    print(f'el error es {mensaje}')
finally:
    #Cerrar el navegador al finalizar.
    driver.quit()
