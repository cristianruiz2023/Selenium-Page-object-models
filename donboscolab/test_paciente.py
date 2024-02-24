
#venv/mnt/42????/ext2/selenium/env_donbosco_pom
#test control de modificacion de pacientes en DonBoscoLabs.com
#controla que la BD refleje los cambios realizados en el front-end

# imports.
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selectores import obtener_selector
