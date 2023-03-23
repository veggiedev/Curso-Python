import time 
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

session = HTMLSession()





url = 'http://www.classcentral.com'
resp = session.get(url)

resp.html.render()




resp.html.html
soup = BeautifulSoup(resp.html.html, 'lxml')











# start by defining the options 
# options = webresp.ChromeOptions() 
# options.headless = False # it's more scalable to work in headless mode 
# # normally, selenium waits for all resources to download 
# # we don't need it as the page also populated with the running javascript code. 
# options.page_load_strategy = 'none' 
# # this returns the path web resp downloaded 
# chrome_path = ChromerespManager().install() 
# chrome_service = Service(chrome_path) 
# # pass the defined options and service objects to initialize the web resp 


# url = 'http://www.classcentra
# url = 'http://www.classcentral.com'
# url = 'http://www.classcentral.com'l.com'
# resp = Chrome(options=options, service=chrome_service) 
# resp.implicitly_wait(5)


# resp.get(url)
# time.sleep(3)
# total_page_height = resp.execute_script("return document.body.scrollHeight")
# browser_window_height = resp.get_window_size(windowHandle='current')['height']
# current_position = resp.execute_script('return window.pageYOffset')

# while total_page_height - current_position > browser_window_height:
#     resp.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
#     current_position = resp.execute_script('return window.pageYOffset')
#     time.sleep(2)
# assert len(resp.window_handles) == 1
# time.sleep(6)
# content = resp.page_source.encode()
# # print(resp.find()) 



# site = requests.get(url = 'http://www.classcentral.com').text


# session = HTMLSession()
# r = session.get(site)
# time.sleep(5)
# # print(r.html)


with open('/home/veggiedev/Curso-Python/Scraping_Project/new_scraped_index.html', 'wb') as f:
     f.write(soup.prettify('utf-8'))