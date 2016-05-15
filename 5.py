import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urllib.request.urlopen(url).read())
print(data)
for line in data:
    print(''.join(elmt[0] * elmt[1] for elmt in line))