import requests
from bs4 import BeautifulSoup

# sample url. Code may change accordingly to url specified
result = requests.get("https://www.whitehouse.gov/briefing-room/")

url_list = []

src = result.content

soup = BeautifulSoup(src, 'lxml')

# find_all returns a list
for h2_tag in soup.find_all("h2"):
    a_tag  = h2_tag.find('a') # find retrieves a single result
    if a_tag is not None:
        url_list.append(a_tag.attrs['href'])

print(url_list)