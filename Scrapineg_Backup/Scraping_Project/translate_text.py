from deep_translator import GoogleTranslator as ts
from bs4 import BeautifulSoup as bs
import os


translator = ts(source='auto', target='hi')

list_text = []

directory = '/home/veggiedev/Curso-Python/Scraping_Project/content'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)




    with open(f, 'r') as document:
        web = f.read()
        soup = bs(web, 'html.parser')
        # print(soup.prettify('utf-8'))
        # text = soup.find_all('a')
        for row in soup.find_all('a'):
            string = row.getText().strip()
            # text = row.text
            # text.replace_with(translator.translate(string))
            list_text.append(string)

    with open(f, 'r') as document:
        web = f.read()
        soup = bs(web, 'html.parser')
        # print(soup.prettify('utf-8'))
        # text = soup.find_all('a')
        for row in soup.find_all('p'):
            string = row.getText().strip()
            # text = row.text
            # text.replace_with(translator.translate(string))
            list_text.append(string)
            print(string)


    with open(f, 'r') as document:
        web = f.read()
        soup = bs(web, 'html.parser')
        # print(soup.prettify('utf-8'))
        # text = soup.find_all('a')
        for row in soup.find_all('h1'):
            string = row.getText().strip()
            # text = row.text
            # text.replace_with(translator.translate(string))
            list_text.append(string)
            print(string)

    with open(f, 'r') as document:
        web = f.read()
        soup = bs(web, 'html.parser')
        # print(soup.prettify('utf-8'))
        # text = soup.find_all('a')
        for row in soup.find_all('h2'):
            string = row.getText().strip()
            # text = row.text
            # text.replace_with(translator.translate(string))
            list_text.append(string)
            print(string)

    with open(f, 'r') as document:
        web = f.read()
        soup = bs(web, 'html.parser')
        # print(soup.prettify('utf-8'))
        # text = soup.find_all('a')
        for row in soup.find_all('h3'):
            string = row.getText().strip()
            # text = row.text
            # text.replace_with(translator.translate(string))
            list_text.append(string)
            print(string)




    old_name = filename
    new_name = f'{filename[:-4]}txt'

    os.rename(old_name, new_name)



    document = open(new_name, 'r')
    filedata = document.read()
    for string in list_text:
        filedata = filedata.replace(string, translator.translate(string))

    newdoc = open(new_name, 'w')
    newdoc.write(filedata)



    txt_name = new_name
    definitive_name = old_name

    os.rename(txt_name, definitive_name)
