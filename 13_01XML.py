#<person>
#  <name>Chuck</name>
#  <phone type="intl">
#     +1 734 303 4456
#   </phone>
#   <email hide="yes" />
#</person>

#XML 1
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Jenny</name>
    <phone type ="intl">
        +1 587 707 9197
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#xml 2
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Jenny</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('user count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
