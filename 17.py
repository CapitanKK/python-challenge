import urllib.request
import bz2
import xmlrpc.client

nothing = 12345
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='

info = ''
while nothing:
    f = urllib.request.urlopen(link + str(nothing))
    content = f.read()
    cookie = f.info().get("Set-Cookie")
    cookie = cookie[cookie.find('info=')+5:cookie.find(';')]
    if cookie == '+':
        cookie = ' '
    if cookie.startswith('%'):
        cookie = chr(int(cookie.replace('%', '0x'), 16))
    info = info + urllib.request.unquote(cookie)
    if 'and the next busynothing is' in str(content):
        nothing = int(str(content)[2:-1].split(" ")[-1])
    else:
        nothing = None

print(bz2.decompress(bytes(info, 'latin1')))

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.phone("Leopold"))

import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('Cookie', 'info=' + 'the flowers are on their way'.replace(' ', '+'))]
f = opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php')
print(f.read())