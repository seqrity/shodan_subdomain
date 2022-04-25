import requests
from bs4 import BeautifulSoup
import re
import sys

domain = sys.argv[1]

URL= 'https://www.shodan.io/domain/'+domain

response_page = requests.get(URL)
my_soup = BeautifulSoup(response_page.content, 'html.parser')
subs = my_soup.find_all('div','card card-padding card-light-blue')

for sub in subs:
    
    find = re.findall('<li>.\w+',str(sub)) 
    match = re.sub('<li>|\[|\]|\'','',str(find))
    final = re.sub('\, ','\n',str(match))
    print(final)
