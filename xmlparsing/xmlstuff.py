import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user id="001">
            <name>John Doe</name>
            <phone type="intl">
                +1 408 555 1234
            </phone>
            <email hide="yes"/>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.get('id'))
    print('Attribute:', item.get("x"))