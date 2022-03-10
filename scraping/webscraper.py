import requests
from bs4 import BeautifulSoup

result = requests.get("https://github.com/")

print(result.status_code)

print(result.headers)

page_src = result.content

#print(page_src)

soup = BeautifulSoup(page_src,'lxml')

links = soup.find_all("a")

for link in links:
    if "Facebook" in link.text:
        print(link)


