from bs4 import BeautifulSoup

with open('home.html','r') as html_read:
    content=html_read.read()

    soup=BeautifulSoup(content,'lxml') #creating the instance of Beautifulsoup. By using it we are parsing the html data#
    courses=soup.find_all('div',class_='card') #if we use 'find or find_all' it will create the output results in list#
    # print(courses)
    for each_course in courses:
        course_name=each_course.h5.text # in this we are getting the 'h5' heading text under each 'div' i.e is the course description'#
        course_price=each_course.a.text.split()[-1] # in this we are getting the 'a' button text(particularly getting the 'price of course' by splitting) under each 'div' i.e is the course description'
        print(f'price of {course_name} is {course_price}')
