from urllib.request import urlopen
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
json_data = urlopen(url, context=ctx).read().decode()
data = json.loads(json_data)

comments = data['comments']
total = sum(int(comment['count']) for comment in comments)

print('Count:', len(comments))
print('Sum:', total)
