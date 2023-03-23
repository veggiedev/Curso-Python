import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



# URL of the web page you want to extract
url = "https://classcentral.com"

driver = uc.Chrome()
html = driver.get(url)


time.sleep(3)



total_page_height = driver.execute_script("return document.body.scrollHeight")
browser_window_height = driver.get_window_size(windowHandle='current')['height']
current_position = driver.execute_script('return window.pageYOffset')

while total_page_height - current_position > browser_window_height:
    driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
    current_position = driver.execute_script('return window.pageYOffset')
    time.sleep(2)
# content = driver.page_source.encode()
# assert len(driver.window_handles) == 1
a = ActionChains(driver)
courses = driver.find_element(By.XPATH, "//*[@id='page-home']/div[1]/header/div[1]/nav/div[1]/button[2]")
a.move_to_element(courses).perform()
time.sleep(3)
empty_space = driver.find_element(By.XPATH, "//*[@id='learning-illus']")
a.move_to_element_with_offset(courses, xoffset=300, yoffset=300).click().perform()
time.sleep(3)
content = driver.page_source.encode()


soup = bs(content, 'lxml')


# # get the JavaScript files
# script_files = []

# for script in soup.find_all("script"):
#     if script.attrs.get("src"):
#         # if the tag has the attribute 'src'
#         script_url = urljoin(url, script.attrs.get("src"))
#         script_files.append(script_url)



# # get the CSS files
# css_files = []

# for css in soup.find_all("link"):
#     if css.attrs.get("href"):
#         # if the link tag has the 'href' attribute
#         css_url = urljoin(url, css.attrs.get("href"))
#         css_files.append(css_url)


# print("Total script files in the page:", len(script_files))
# print("Total CSS files in the page:", len(css_files))

# # write file links into files
# with open("javascript_files.txt", "w") as f:
#     for js_file in script_files:
#         print(js_file, file=f)

# with open("css_files.txt", "w") as f:
#     for css_file in css_files:
#         print(css_file, file=f)



with open("full_index.html", "wb") as f:
    f.write(content)