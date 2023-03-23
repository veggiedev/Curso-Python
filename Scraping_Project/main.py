import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


# options.add_argument("--headless")
# options.add_argument("--disable-blink-features=AutomationControlled")
prefs = {
    "translate":{"enabled":"true"},
    "translate_whitelists":{"en":"hi"}
  
}
options = uc.ChromeOptions()
options.add_argument("--lang=hi")
options.add_experimental_option("prefs", prefs)
# options.add_argument("--headless")
driver = uc.Chrome(options=options) 
driver.get("https://www.classcentral.com/") 


total_page_height = driver.execute_script("return document.body.scrollHeight")
browser_window_height = driver.get_window_size(windowHandle='current')['height']
current_position = driver.execute_script('return window.pageYOffset')

while total_page_height - current_position > browser_window_height:
    driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
    current_position = driver.execute_script('return window.pageYOffset')
    time.sleep(2)
content = driver.page_source.encode()
assert len(driver.window_handles) == 1
driver.refresh()
time.sleep(5)
wait = WebDriverWait(driver, 10)


# file = open('index.html', 'wb')
# file.write(content)

# original_window = driver.current_window_handle


links = driver.find_elements(By.XPATH, "//a[@href]")
links_list = []
for i in links:
    links_list.append(i.get_attribute('href'))


url_list = open('url_list.txt', 'w')
for item in links_list:
    url_list.write("%s\n" % item)

# print(len(links))
# print(links_list)
for web_address in links_list:
    # print(i.get_attribute('href'))
    driver.get(web_address)
    total_page_height = driver.execute_script("return document.body.scrollHeight")
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')

    while total_page_height - current_position > browser_window_height:
        driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        current_position = driver.execute_script('return window.pageYOffset')
        time.sleep(1)
    newcontent = driver.page_source.encode('utf-8')
    assert len(driver.window_handles) == 1
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    classcentral = 'https://www.classcentral.com'
    if web_address == 'https://www.classcentral.com':
        stripped_url = '#'
        file = open(stripped_url, 'w')
        file.write(newcontent)
    else:
        if classcentral in web_address:
            stripped_url = web_address[28:]
            # print(stripped_url)
            file_name_list = []
            for c in reversed(stripped_url):
                # print(c)
                if c != '/':
                    file_name_list.append(c)
                else:
                    break
            file_name = ''.join(reversed(file_name_list))

            print(f'This is the file name:{file_name}')

            # stripped_url_final = stripped_url[28:]
            # print(stripped_url.count('/'))
            # print(stripped_url)
            
            if stripped_url != "/":
                print('stripped url is not /')
                number_of_slash = stripped_url.count('/')
                print(f'Number of slashes in stripped url: {number_of_slash}')
                if  number_of_slash > 1:
                    print('number of slashes is bigger than 1')
                    directory = stripped_url.replace(file_name, '')
                    print(f'This is the directory:{directory}here it ends')
                    if directory != '/':
                        print('directory is no /')
                        # os.makedirs(os.path.dirname(directory), exist_ok=True)
                        # final_url = stripped_url[-1].replace('/', '')
                        # print(final_url)
                        # last_url = final_url + '.html'
                        # print(f'Last url:{last_url}')
                        file = open(f'{file_name}.html', 'wb')
                        file.write(newcontent)
                else:
                    print('Number of slashes is smaller than 1')
                    directory = stripped_url.replace(file_name, '')
                    # print(f'This is the directory:{directory}here it ends')
                    # print(f'This is dir name: {directory}')
                    os.makedirs(os.path.dirname(directory), exist_ok=True)
                    # final_url = stripped_url[-1].replace('/', '')
                    print(f'This is the file name before file creation:{file_name}')
                    # last_url = final_url + '.html'
                    # print(f'Last url:{last_url}')
                    file = open(f'{file_name}.html', 'wb')
                    print(newcontent)
                    file.write(newcontent)


            else:
                pass

        else:
            pass










    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    # driver.refresh()
    # time.sleep(5)
    for link in links:
        driver.execute_script("arguments[0].scrollIntoView();", link)
        web_address = link.get_attribute("href")
        # title = link.current_url
        driver.get(f'{web_address}')
        url = driver.current_url
        stripped_url = url.strip('https://www.classcentral.com/')
        print(stripped_url)
        

        
        # link.click()
        # time.sleep(3)
        # for window_handle in driver.window_handles:
        #     if window_handle != original_window:
        #         driver.switch_to.window(window_handle)
        #         break
        # time.sleep(3)
        # content = driver.page_source.encode()
        # site_title = driver.title()
        # file = open(f'{site_title}'.html, 'wb')
        # file.write(content)
    # print(links.count())



    # driver.find_elements()



