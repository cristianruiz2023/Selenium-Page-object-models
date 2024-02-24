import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#carga el driver 
driver=webdriver.Chrome()
driver.maximize_window()
#carga la url
driver.get("https://institutoweb.com.ar/test/test2/select.html")
time.sleep(2)
# localizar elementos
select_element = driver.find_element(By.NAME,'selector')
select_element.send_keys('España')
# sendkey selecciona el selector por letras parcial o total 
time.sleep(1)
select_element.send_keys('Canada')
time.sleep(1)
select_element.send_keys('Colombia ')
time.sleep(2)
#primero busca el elemento(por name css xpath) y se aloja en una variable 
# luego se hace otra variable y se le da la instrucion Select con la variable
#donde localizamos el elemento(select_element)
mi_selector = Select(select_element)#aca le dicimos a selenium es un desplegable
time.sleep(1)
mi_selector.select_by_value('value2')
time.sleep(1)
#busca por value index o por texto visible el Select
mi_selector.select_by_index(0)
time.sleep(1)
mi_selector.select_by_visible_text('Colombia')
time.sleep(1)
mi_selector.select_by_index(2)
time.sleep(1)
driver.quit()