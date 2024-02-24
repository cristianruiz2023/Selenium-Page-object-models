# selectores.py
# Aquí guardaremos los selectores utilizados en el test
#los agrupamos por pantalla

def obtener_selector():
    """retorna los selectores de la pantalla login
    datos obtenidos: 
    driver.find_element(By.ID,'username')
    driver.find_element(By.ID,'password')
    driver.find_element(By.ID,'loginButton')
    """
    selectores_login = {
        "input_usuario" : "username",
        "input_password" : "password",
        "btn_ingresar" : "loginButton"
}
    return selectores_login