from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))

for _ in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    # Positions in the exercise begin at 1; Python list indexes begin at 0.
    tag = tags[position - 1]
    name = tag.get_text(strip=True)
    url = tag.get('href')
    print('Retrieving:', url)

print('Last name:', name)
