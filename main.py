# importing the library for web_scrapping
from bs4 import BeautifulSoup

# reading the html file
with open('home.html','r') as html_file:
    content=html_file.read()
    # print(content)
    soup=BeautifulSoup(content,'lxml')  #by using beautifulsoup we are parsing the html data#
    # print(soup)
    tags=soup.find_all('h5')
    print(tags)

    for i in tags:
        print(i.text)
