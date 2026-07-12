import xml.etree.ElementTree as ET
data = '''<person>
    <name>John Doe</name>
    <phone type="intl">
        +1 408 555 1234
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)  
print('Attr:', tree.find('email').get('hide'))