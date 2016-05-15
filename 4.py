import urllib.request

# nothing = 12345
nothing = 25357
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

while nothing:
    f = urllib.request.urlopen(link + str(nothing))
    content = f.read()
    print(content)
    nothing = int(str(content)[2:-1].split(" ")[-1])