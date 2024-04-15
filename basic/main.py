from bs4 import BeautifulSoup

with open('home.html','r') as html_f:
    content = html_f.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div',class_='card')
    for c in course_cards:
        c_name = c.h5.text
        c_price = c.a.text.split()[-1]

        print(f'{c_name} costs {c_price}')
    