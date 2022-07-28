
from ast import MatchSequence
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from difflib import SequenceMatcher
import csv

###############CONSUM###################


########creacion de elementos y manipulacion de la pagina web###############

website = "https://tienda.consum.es/es/s/'producto_a_buscar'?orderById=7"
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(website)


#########tiempo de espera para que salga y desacernos de la ventana 'cookies'#######

sleep(3)
cookies_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[2]/div/div/button')
cookies_button.click()

busqueda = 'chocolate milka'
sleep(2)
boton_busqueda = driver.find_element(By.XPATH, '/html/body/app-root/app-root/ng-component/div/ng-component/div/div[1]/cmp-header/div[1]/div[2]/div/div/div[3]/div/cmp-searcher/div/cmp-triple-element-block/div/div[1]/input' )
sleep(2)
boton_busqueda.send_keys(busqueda)
sleep(2)
boton_busqueda.send_keys(Keys.RETURN)

sleep(3)
driver.current_url
ventana_con=driver.find_element(By.XPATH, '//*[@id="grid-title"]')
ventana_con.click()
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)

boton_ver_mas = driver.find_element(By.XPATH, '/html/body/app-root/app-root/ng-component/div/ng-component/div/div[2]/div/mod-catalog/div/lib-grid/div/div/div[2]/div[2]/cmp-products-grid/div[2]/div[2]/button')

boton_ver_mas.click()
sleep(2)

items = driver.find_elements(By.XPATH, '//*[@id="grid-widget--descr"]')
precios = driver.find_elements(By.XPATH, '//*[@id="grid-widget--price"]')
productos_consum = []
precios_consum = []



for precio in precios:
    precios_consum.append(precio.text)
for nombre in items:
    productos_consum.append(nombre.text)






driver.close()



####################CARREFOUR#################
carrefour = 'https://www.carrefour.es/?q=chocolate+milka'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

wd.get(carrefour)

sleep(4)
cookies_button = wd.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
cookies_button.click()
sleep(2)
ventana = wd.find_element(By.XPATH, '/html/body/section/main/div/aside[1]/div/p')
ventana.click()
sleep(6)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)
wd.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
sleep(4)

sleep(10)

sacar_precio_carr = wd.find_elements(By.CLASS_NAME, 'ebx-result-price__value')
sleep(8)
precios_carr = []
productos_carr = []
for precio in sacar_precio_carr:
    precios_carr.append(precio.text)
sleep(4)
sacar_producto_carr = wd.find_elements(By.XPATH, '//*[@id="ebx-grid"]/article/div/a[2]')

for producto in sacar_producto_carr:
    productos_carr.append(producto.text)
print(len(productos_carr))
print(len(precios_carr))

dict_carrefour = {}
dict_consum = {}




wd.close()

def is_string_similar(s1: str, s2: str, threshold: float = 0.66): #-> bool    
    return SequenceMatcher(a=s1, b=s2).ratio() > threshold

producto_similares_con = []
producto_similares_carr = []
def porcentaje(pr1, pr2):
    return SequenceMatcher(a=pr1, b=pr2).ratio()

lista_productos_similares = []
for producto_carr in productos_carr:
    for producto_con in productos_consum:           
        if is_string_similar(s1=producto_carr, s2=producto_con) == True:

            lista_productos_similares.append({'Producto de Consum':{producto_con:precios_consum[productos_consum.index(producto_con)]}, 'Producto de Carrefour':{producto_carr:precios_carr[productos_carr.index(producto_carr)]}, 'Porcentaje Similitud':porcentaje(producto_carr, producto_con)})
print(lista_productos_similares)
columnas = ['Producto de Consum', 'Producto de Carrefour', 'Porcentaje Similitud']
try:
    with open("productos.csv", 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnas)
        writer.writeheader()
        for key in lista_productos_similares:
            writer.writerow(key)
except IOError:
    print("I/O error")
