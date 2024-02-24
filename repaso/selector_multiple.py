


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#carga el driver 
driver=webdriver.Chrome()
driver.maximize_window()
#carga la url
driver.get("https://institutoweb.com.ar/test/test2/selectmultiple.html")
time.sleep(2)
# localizar el elemnto por id
select_element = driver.find_element(By.ID,'selector')
multiple = Select(select_element)
multiple.deselect_by_value('value2')
time.sleep(1)
multiple.select_by_value('value1')
time.sleep(1)
multiple.select_by_value('value3')
time.sleep(1)
multiple.select_by_value('value2')
time.sleep(1)
multiple.deselect_all()
time.sleep(1)
driver.quit()