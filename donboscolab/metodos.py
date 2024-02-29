

from selenium.webdriver.common.by import By

def escribir_id(driver,elemento,texto):
    driver.find_element(By.ID, elemento).click()# selecciona el campo
    driver.find_element(By.ID, elemento).clear()# limpia el campo
    driver.find_element(By.ID, elemento).send_keys(texto) # envía el texto

def click_link(driver,texto):
    driver.find_element(By.LINK_TEXT, texto).click()

def click_id(driver,elemento):
    driver.find_element(By.ID, elemento).click()

def visitar_web(driver,url):
    driver.get(url)

# def espera_implicita(driver,segundos):
 #   driver.implicitly_wait(segundos)
def espera_implicita(driver):
    driver.implicitly_wait(4)
